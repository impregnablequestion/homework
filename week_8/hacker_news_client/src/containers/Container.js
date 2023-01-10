import React from "react";
import { useState, useEffect } from "react";
import StoryList from "../components/StoryList";

const Container = () => {

    const [storyObjects, setStoryObjects] = useState([]);
    const [textInput, setTextInput] = useState("");

    useEffect(() => {
        fetch("https://hacker-news.firebaseio.com/v0/topstories.json")
            .then(result => result.json())
            .then(ids => {
                const storyPromises = ids.slice(0,20).map(id => {
                    return fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`).then(response=>response.json())
                });
                Promise.all(storyPromises)
                    .then(objects => {
                        setStoryObjects(objects)
                    }
            )
        });
    }, [])

    const handleInput = (event) => {
        setTextInput(event.target.value);
    }

    return(
        <div className="content">
            <input type="text" onChange={handleInput} value={textInput}/>
            <StoryList stories = {storyObjects} filter={textInput}></StoryList>
        </div>
    );

}

export default Container;