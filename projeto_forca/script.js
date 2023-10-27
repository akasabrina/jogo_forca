
word = [this.word[Math.floor(Math.random() * this.word.length)]]
let guessedWord = [];
let wrongLetters = [];
for(let i = 0; i < word.length; i++) {
    guessedWord[i] = '_';
}


function guess() {
    document.getElementById('letter').addEventListener('letter', function() {
        if(this.value.length > 1) {
            alert('Insira somente um caracter')
        }
        else;
    });
    let letter = document.getElementById('letter').value.toUpperCase();
    if(word.includes(letter)) {
        for(let i = 0; i < word.length; i++) {
            if(word[i] === letter) {
                guessedWord[i] = letter;
            }
        }
    } else {
        wrongLetters.push(letter);
        document.getElementById('hangman').innerHTML += addEventListener('Adicionar Image');
        document.getElementById('wrong-letters').innerHTML = 'Letras erradas: ' + wrongLetters.join(', ');
    }
    
    document.getElementById('word').innerHTML = guessedWord.join(' ');
    
    if(guessedWord.join('') === word) {
        alert('Parabéns! Você ganhou!');
    }
}

document.getElementById('word').innerHTML = guessedWord.join(' ');
// this.boneco = "";
// this.erros = 0;
