// Name: Mingxi Zhu

// Problem: Minimum Cost To Convert String II

// Description:
//  You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English characters. 
//  You are also given two 0-indexed string arrays original and changed, and an integer array cost, where cost[i] represents 
//  the cost of converting the string original[i] to the string changed[i].

//  You start with the string source. In one operation, you can pick a substring x from the string, and change it to y at a 
//  cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y. You are allowed to 
//  do any number of operations, but any pair of operations must satisfy either of these two conditions:

//  The substrings picked in the operations are source[a..b] and source[c..d] with either b < c or d < a. In other words, 
//  the indices picked in both operations are disjoint.

//  The substrings picked in the operations are source[a..b] and source[c..d] with a == c and b == d. In other words, the 
//  indices picked in both operations are identical.

//  Return the minimum cost to convert the string source to the string target using any number of operations. If it is 
//  impossible to convert source to target, return -1.

//  Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

// Constraints:
//  1 <= source.length == target.length <= 1000
//  source, target consist only of lowercase English characters.
//  1 <= cost.length == original.length == changed.length <= 100
//  1 <= original[i].length == changed[i].length <= source.length
//  original[i], changed[i] consist only of lowercase English characters.
//  original[i] != changed[i]
//  1 <= cost[i] <= 106

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <chrono>
#include <fstream>
#include <climits>

using namespace std;

// Implement TrieNode class
class TrieNode {
    public:
    TrieNode* next[26];
    int idx;
    TrieNode() {
        for (int i=0; i<26; i++) {
            next[i]=nullptr;
        }
        idx=-1;
    }
};

// Implement the main algorithm
class Solution {
    private:
    TrieNode* root;
    void clearTrie(TrieNode* node) {
        if (!node) return;
        for (int i = 0; i < 26; i++) {
            clearTrie(node->next[i]);
        }
        delete node;
    }
    public:
        Solution() {
            root = new TrieNode();
        }
        ~Solution() {
            clearTrie(root);
        }
        
        long long minCostToRepStr(string source, string target, 
            vector<string>& original, vector<string>& changed, vector<int>& cost) {
            // Step1: reverse strings in vector original and changed for dynamic programming.
            for (auto& s : original) reverse(s.begin(), s.end());
            for (auto& s : changed) reverse(s.begin(), s.end());

            // Step2: remove duplicated strings in vector original and changed.
            unordered_set<string> Set;
            Set.insert(original.begin(), original.end());
            Set.insert(changed.begin(), changed.end());

            // Step3: see all strings in vector original and changed as nodes being traversed.
            //        using Trie to index all nodes.
            //        T(n) = O(n*m), n=original_size<=100, m=average word size<=1000
            int idx = 0;
            int node_size = Set.size();
            for (string node : Set) {
                TrieNode* t_node = root;
                for (char c : node) {
                    if (t_node->next[c-'a']==nullptr) 
                        t_node->next[c-'a'] = new TrieNode();
                    t_node = t_node->next[c-'a'];
                }
                t_node->idx = idx;
                idx++;
            }

            // Step4: pre-compute minimum cost among all nodes(v)
            //        using Flyod-Warshall Algorithm.
            //        T(n)=O(v^3), v=nodes_size<=200
            vector<vector<long long>> min_cost(node_size, vector<long long>(node_size, LLONG_MAX/3));
            for (int i=0; i<node_size; i++) min_cost[i][i] = 0;
            for (int i=0; i<original.size(); i++) {
                TrieNode* org = root;
                for (char c : original[i]) org = org->next[c-'a'];
                TrieNode* chg = root;
                for (char c : changed[i]) chg = chg->next[c-'a'];
                min_cost[org->idx][chg->idx] = min(min_cost[org->idx][chg->idx], (long long)cost[i]);
            }
            for (int k=0; k<node_size; k++) {
                for (int i=0; i<node_size; i++) {
                    for (int j=0; j<node_size; j++) {
                        min_cost[i][j] = min(min_cost[i][j], min_cost[i][k]+min_cost[k][j]);
                    }
                }
            }

            // Step5: find nodes in source string and change it to match target string
            //        using Dynamic Programming.
            //        base case: dp[0] = 0 because change it to itself costs 0
            //                   dp[i] = inf
            //        iteration: dp[i] = min(dp[i], dp[j-1]+min_cost[original str idx][changed str idx])
            //        T(n) = O(m^2), m=string_size<=1000
            source = "#"+source;
            target = "#"+target;
            int str_size = source.size();
            vector<long long> dp(str_size, LLONG_MAX/3);
            dp[0] = 0;
            for (int i=1; i<str_size; i++) {
                if (source[i] == target[i]) 
                    dp[i] = min(dp[i], dp[i-1]);
                
                TrieNode* org = root;
                TrieNode* chg = root;
                for (int j=i; j>=1; j--) {
                    if (org->next[source[j]-'a']==nullptr ||
                        chg->next[target[j]-'a']==nullptr)
                        break;
                    
                    org = org->next[source[j]-'a'];
                    chg = chg->next[target[j]-'a'];
                    if (org->idx!=-1 && chg->idx!=-1) {
                        dp[i] = min(dp[i], dp[j-1]+min_cost[org->idx][chg->idx]);
                    }
                }
            }

            // Step6: return dp[n] if dp[n] != inf
            if (dp[str_size-1] == LLONG_MAX/3)
                return -1;
            return dp[str_size-1];
        }
};

// Helper for generating random test data
class Test {
public:
struct TestCase {
    string source;
    string target;
    vector<string> original;
    vector<string> changed;
    vector<int> cost;
};

TestCase generateInput(int strLen, int numRules) {
    TestCase tc;
    
    // 1. Generate Source
    for(int i = 0; i < strLen; ++i) tc.source += (char)('a' + rand() % 26);
    tc.target = tc.source;

    // 2. Generate Rules (and apply some to Target to ensure a path exists)
    for(int i = 0; i < numRules; ++i) {
        int ruleLen = 1 + (rand() % 5); // Keep rules short for logic density
        string s_orig = "";
        string s_chg = "";
        for(int j = 0; j < ruleLen; ++j) {
            s_orig += (char)('a' + rand() % 26);
            s_chg += (char)('a' + rand() % 26);
        }
        
        if (s_orig == s_chg) s_chg[0] = (s_chg[0] == 'z' ? 'a' : s_chg[0] + 1);

        tc.original.push_back(s_orig);
        tc.changed.push_back(s_chg);
        tc.cost.push_back(1 + (rand() % 1000));

        // Inject this rule into the target string randomly to guarantee solvability
        if (rand() % 5 == 0 && tc.target.length() >= (size_t)ruleLen) {
            size_t pos = rand() % (tc.target.length() - ruleLen + 1);
            if (tc.target.substr(pos, ruleLen) == s_orig) {
                tc.target.replace(pos, ruleLen, s_chg);
            }
        }
    }
    return tc;
}
};

// Time analysis
int main() {
    Solution sol;
    Test test;
    // Test targets: 10 rules, 100 rules, 1000
    vector<double> time_10;
    vector<double> time_50;
    vector<double> time_100;

    for (int i=10; i<=1000; i+=10) {
        int strLen = i;
        int numRules = 10;

        Test::TestCase tc =test.generateInput(strLen, numRules);

        auto start = chrono::high_resolution_clock::now();
        long long result = sol.minCostToRepStr(tc.source, tc.target, tc.original, tc.changed, tc.cost);
        auto end = chrono::high_resolution_clock::now();

        chrono::duration<double, milli> elapsed = end - start;
        time_10.push_back(elapsed.count());
    }

    for (int i=10; i<=1000; i+=10) {
        int strLen = i;
        int numRules = 50;

        Test::TestCase tc =test.generateInput(strLen, numRules);

        auto start = chrono::high_resolution_clock::now();
        long long result = sol.minCostToRepStr(tc.source, tc.target, tc.original, tc.changed, tc.cost);
        auto end = chrono::high_resolution_clock::now();

        chrono::duration<double, milli> elapsed = end - start;
        time_50.push_back(elapsed.count());
    }

    for (int i=10; i<=1000; i+=10) {
        int strLen = i;
        int numRules = 100;

        Test::TestCase tc =test.generateInput(strLen, numRules);

        auto start = chrono::high_resolution_clock::now();
        long long result = sol.minCostToRepStr(tc.source, tc.target, tc.original, tc.changed, tc.cost);
        auto end = chrono::high_resolution_clock::now();

        chrono::duration<double, milli> elapsed = end - start;
        time_100.push_back(elapsed.count());
    }
    ofstream outFile("time.csv");
    if (outFile) {
        for (int i=0; i<time_10.size(); i++) {
            outFile << time_10[i];
            if (i<time_10.size()-1)
                outFile << ",";
        }
        outFile << "\n";

        for (int i=0; i<time_50.size(); i++) {
            outFile << time_50[i];
            if (i<time_50.size()-1)
                outFile << ",";
        }
        outFile << "\n";
    
        for (int i=0; i<time_100.size(); i++) {
            outFile << time_100[i];
            if (i<time_100.size()-1)
                outFile << ",";
        }
    }
    outFile.close();
    
    return 0;
}
