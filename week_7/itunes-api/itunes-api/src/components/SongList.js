import Song from "./Song";
import "./SongList.css";

const SongList = ({songs}) => {

    const listOfSongs = songs.map((song, index) => {
        return <Song song={song} key={index} index={index}/>;
    });

    return(
        <div className="SongList">
            {listOfSongs}
        </div>
    );
}

export default SongList;
