import React from "react";
import { useState, useEffect } from "react";
import SearchBar from "../components/SearchBar";
import StoryList from "../components/StoryList";

const Container = () => {

    const [storyIDs, setStoryIDs] = useState([]);
    const [storyObjects, setStoryObjects] = useState([]);

    useEffect(() => {
        fetch("https://hacker-news.firebaseio.com/v0/topstories.json")
            .then(result => result.json())
            .then(ids => setStoryIDs(ids));

    }, [])

    useEffect(() => {

        const results = storyIDs.map((id)=>{
            return fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`)
                .then(response => response.json())
        })

        Promise.all(results)
            .then(objects => {
                setStoryObjects(objects);
            })

    }, [storyIDs])

    console.log(storyObjects);

    return(
        <div className="content">
            <SearchBar></SearchBar>
            <StoryList></StoryList>
        </div>
    );

}

export default Container;