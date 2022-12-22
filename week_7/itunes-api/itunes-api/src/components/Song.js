import "./Song.css"
import { useState } from "react"

const Song = ({song, index}) => {

    const [songPlaying, setSongPlaying] = useState(false)

    const album_artwork = song['im:image'][2].label
    const preview = song.link[1].attributes.href

    const handleClick = function () {
        setSongPlaying(!songPlaying);
        console.log(`${song['im:name'].label} has been clicked`)
    }

    return(
        <div className="song">
            <img src={album_artwork} alt="album artwork"></img>
            <p>{index+1}: {song['im:name'].label}</p>
            <p className="artist">{song['im:artist'].label}</p>
            <audio controls src={preview} onClick={() => {handleClick()}} className={songPlaying? "spinny":"still"}>download</audio>
        </div>
    );
}

export default Song;