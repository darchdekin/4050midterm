#include <string>
#include <cctype>
#include <unordered_set>
#include <iostream>
using namespace std;

bool isNice(unordered_set<char> set);
unordered_set<char> charSet(string s);
bool isNice(char c, unordered_set<char> set);

string longestNiceSubstring(string s) {
    if(s.length()<=1) return "";
    unordered_set<char> set = charSet(s);
    if(isNice(set)) return s;
    else if(s.length()==2) return "";

    int splitIndex;
    for(int i = 0; i < s.length(); i++){
        if(!isNice(s[i], set)){
            splitIndex = i;
            break;
        }
    }

    //case the first substring doesn't have enough characters to be a nice substring
    if(splitIndex < 2){
        return longestNiceSubstring( s.substr(splitIndex+1, string::npos) );
    }
    //case the second substring doesn't have enough characters to be a nice substring
    else if(splitIndex > s.length() - 3){
        return longestNiceSubstring(s.substr(0, splitIndex));
    }
    //case both the first and second substrings have enough characters to be a nice substring
    else {
        string a = s.substr(0, splitIndex);
        string b = s.substr(splitIndex+1, string::npos);
        string c = longestNiceSubstring(a);
        string d = longestNiceSubstring(b);
        int cLen = c.length();
        int dLen = d.length();
        if(cLen >= dLen) return c;
        else return d;
    }
} 

//Returns an unordered set containing all the characters in s
unordered_set<char> charSet(string s){
    unordered_set<char> set;
    int l = s.length();
    for(int i = 0; i < l; i++){
        set.insert(s[i]);
    }
    return set;
}


//Checks that for every character c in set, c appears as both uppercase and lowercase
bool isNice(unordered_set<char> set){
    if(set.size() < 2) return false;
    for (auto it = set.begin(); it != set.end(); ++it){
        if(!isalpha(*it)) return false;
        if(isupper(*it)){
            if(set.count(tolower(*it))==0) return false;
        } else {
            if(set.count(toupper(*it))==0) return false;
        }
    }
    return true;
}

//Checks that c appears in set as both uppercase and lowercase
bool isNice(char c, unordered_set<char> set){
    if(!isalpha(c)) return false;
    if(isupper(c)) return set.count(tolower(c));
    else return set.count(toupper(c));
}

int main(){
    string s = "abcdefghijklmnopqrstuUuVvwxyz";
    cout << "LNS: " << longestNiceSubstring(s) << "\n";
}