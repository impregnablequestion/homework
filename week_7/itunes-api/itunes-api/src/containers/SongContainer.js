import { useState } from "react";
import { useEffect } from "react";
import SongList from "../components/SongList";
import './SongContainer.css'

const SongContainer = () => {

    const [songs, setSongs] = useState([]);
    const [genre, setGenre] = useState("Rock");
    
    useEffect(()=>{
        getSongs(genre);
    }, [songs, genre]
    );

    const handleChange = (event) => {
        setGenre(event.target.value)
    }

    const getSongs = function (genre) {
        if (genre === null || genre === "") {
            fetch('https://itunes.apple.com/gb/rss/topsongs/limit=20/json')
            .then(data => data.json())
            .then(songs => setSongs(songs.feed.entry));
        }
        else if (genre === "Rock") {
            fetch('https://itunes.apple.com/gb/rss/topsongs/limit=20/genre=21/json')
            .then(data => data.json())
            .then(songs => setSongs(songs.feed.entry));
        }
        else if (genre === "Dance") {
            fetch('https://itunes.apple.com/gb/rss/topsongs/limit=20/genre=17/json')
            .then(data => data.json())
            .then(songs => setSongs(songs.feed.entry));
        }
        else if (genre === "Country") {
            fetch('https://itunes.apple.com/gb/rss/topsongs/limit=20/genre=6/json')
            .then(data => data.json())
            .then(songs => setSongs(songs.feed.entry));
        }
        
    }

    return(
        <div className="song-container">
            <h1>Current UK Top 20</h1>
            <div id="dropdown-wrapper">
            <label htmlFor="genre"><h2>pick a genre:</h2></label>
            <select onChange={handleChange}>
                <option value="">all</option>
                <option value="Rock">rock</option>
                <option value="Country">country</option>
                <option value="Dance">dance</option>
            </select>
            </div>
            <SongList songs={songs}></SongList>
        </div>
    );
}

export default SongContainer;