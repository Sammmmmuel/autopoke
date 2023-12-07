from flask import *
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["name"])
        print(request.form["email"])
        return

    return render_template("index.html")
if __name__ == "__main__":
    app.run()
class TrieNode:
 
    #constructor, Time O(1) Space O(1)
    def __init__(self, c):
        self.data = c
        self.isEnd = False
        self.children = {} #map
 
class Trie:
    #constructor, Time O(1) Space O(1)
    def __init__(self):
        self.root = TrieNode('')
    
    #Add a word to trie, Time O(s) Space O(1) s is word length
    def insert(self, word):
        node = self.root
        for ch in word:
            if not ch in node.children:
                node.children[ch] = TrieNode(ch)   
            node = node.children[ch]                  
        node.isEnd = True
   
    #find all word with given prefix
	#Time O(n), Space O(n), n is number of nodes involved (include prefix and branches)
    def autocomplete(self, word):
        res = []
        node = self.root
        for ch in word:           
            if ch in node.children:
                node = node.children[ch]
            else:
                return []
        self.helper(node, res, word[:-1]) #except the last "ama", node is "z"
        return res
 
    #recursive function called by autocomplete
	#Time O(n), Space O(n), n is number of nodes in branches
    def helper(self, node, res, prefix):
        if node.isEnd:
            res.append(prefix + node.data)       
        for child in node.children.values():
            self.helper(child, res, prefix + node.data)
 
t = Trie()      
pokemon = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
t.insert("Bublbasaur")
t.insert("Ivysaur")
t.insert("Venusaur")
t.insert("Charmander")
t.insert("Charmeleon")
t.insert("Charizard")
a = t.autocomplete("Char")
print(a)