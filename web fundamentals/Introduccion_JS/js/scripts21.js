// Methods of ownership

const player = {
    play: function(id){
        console.log(`Play Music with the id: ${id}`)
    },
    pause: function(){
        console.log(`Pausing.....`)
    },
    createPlaylist: function(name){
        console.log(`Creating the playlist with the name ${name}`)
    },
    playPlayLits: function(name){
        console.log(`play the playlist: ${name}`)
    }
}

player.deleteSong = function(id){
    console.log(`Deleting the song with the id: ${id}`)
}

console.log(player);
player.play(2039);
player.pause();
player.deleteSong(2020);
player.createPlaylist(`yerbatero`);
player.playPlayLits(`HeartBreaker`);
