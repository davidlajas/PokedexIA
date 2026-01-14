const BACKEND_URL = "/chat";
async function buscarPokemon() {
    const inputName = document.getElementById("pokemonInput").value.trim().toLowerCase();
    if (!inputName) return;

    const nameEl = document.getElementById("pokemonName");
    const spriteEl = document.getElementById("pokemonSprite");
    const mainDataEl = document.getElementById("mainData");
    const statsEl = document.getElementById("statsDisplay");

    nameEl.textContent = "ESCANEANDO...";
    mainDataEl.innerHTML = "Zzt... Accediendo a archivos de Alola...";
    statsEl.innerHTML = "Decodificando parámetros...";
    spriteEl.style.display = "none";

    try {
        
        const pokeRes = await fetch(`https://pokeapi.co/api/v2/pokemon/${inputName}`);
        let realName = inputName;
        if (pokeRes.ok) {
            const pokeData = await pokeRes.json();
            spriteEl.src = pokeData.sprites.other['official-artwork'].front_default;
            spriteEl.style.display = "block";
            realName = pokeData.name.toUpperCase();
        }

        
        const res = await fetch(BACKEND_URL, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ message: inputName })
        });

        if (res.ok) {
            const data = await res.json();
            const fullText = data.response;

            
            const lowerText = fullText.toLowerCase();
            const keywords = ["estadísticas", "stats", "puntos de combate", "base:"];
            let splitIndex = fullText.length; 

            for (let word of keywords) {
                let foundPos = lowerText.indexOf(word);
                if (foundPos !== -1 && foundPos < splitIndex) {
                    splitIndex = foundPos;
                }
            }

            const leftPart = fullText.substring(0, splitIndex);
            const rightPart = fullText.substring(splitIndex);

            nameEl.textContent = realName;
            mainDataEl.innerHTML = formatMarkdown(leftPart);
            statsEl.innerHTML = formatMarkdown(rightPart || "Zzt... No se detectaron estadísticas específicas.");
        }
    } catch (err) {
        mainDataEl.textContent = "Error de conexión, zzt!";
    }
}

function formatMarkdown(text) {
    if (!text) return "";

    return text
        
        .replace(/^#+\s*(.*)$/gm, "<h3>$1</h3>")
        
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        
        .replace(/\*(.*?)\*/g, "<em>$1</em>")
        
        .replace(/^\s*-\s*(.*)$/gm, "• $1")
        
        .replace(/\n/g, "<br>");
}
