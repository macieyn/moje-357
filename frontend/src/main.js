class Moje357 {
    constructor() {
      this.data = null;
      this.playlistsContainer = null;
      this.playlists = null;
    }

    render_playlist() {
        this.playlistsContainer = $('#playlist-container');
        this.playlists = this.data.playlists;
        this.playlists.forEach((playlist) => {
            const playlistDiv = document.createElement('div');
            playlistDiv.classList.add('col-md-12', 'mt-3');
            const playlistNameH3 = document.createElement('h3');
            playlistNameH3.textContent = playlist.name;
            playlistDiv.append(playlistNameH3);
            playlistDiv.append(document.createElement('hr'));

            playlist.play_events.forEach((track, index) => {
                const trackDiv = document.createElement('div');
                let datetime = new Date(Date.parse(track.played_at));
                console.log(datetime);
                $(trackDiv).append(`
                    <div class="col-md-12">
                        <div class="row mb-1">
                            <div class="col-1">${index + 1}.</div>
                            <div class="col-11 col-sm-7">${track.track.name}</div>
                            <div class="col-1"></div>
                            <div class="col-5 col-sm-2">${datetime.toLocaleTimeString()}</div>
                            <div class="col-5 col-sm-1 text-right">
                                <a href="http://open.spotify.com/track/${track.track.spotify_id}" target="blank">
                                    <img src="spotify_icon_black.png" width="21px" height="21px">
                                </a>
                            </div>
                        </div>
                    </div>
                `);
                playlistDiv.append(trackDiv);

            })
            

            this.playlistsContainer.append(playlistDiv)

        })
    }


}

const m357 = new Moje357();

$(document).ready(() => {
    
    $.getJSON("http://127.0.0.1:5000/api/playlists")
        .done((resp) => {
            m357.data = resp;
            console.log(m357.data);
            m357.render_playlist();
        })
        .fail((err) => {
            console.log(err);
        })
})



