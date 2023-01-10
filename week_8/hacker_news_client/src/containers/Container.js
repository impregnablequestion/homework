import React from "react";
import { useState, useEffect } from "react";
import StoryList from "../components/StoryList";
import StringSimilarity from "../filtering_logic/FuzzyFilter";

const Container = () => {

    const [storyObjects, setStoryObjects] = useState([]);
    const [fuzzyTextInput, setFuzzyTextInput] = useState("");
    const [clearTextInput, setClearTextInput] = useState("");

    useEffect(() => {
        fetch("https://hacker-news.firebaseio.com/v0/topstories.json")
            .then(result => result.json())
            .then(ids => {
                const storyPromises = ids.slice(0,).map(id => {
                    return fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`).then(response=>response.json())
                });
                Promise.all(storyPromises)
                    .then(objects => {
                        setStoryObjects(objects)
                    }
            )
        });
    }, [])

    const handleFuzzyInput = (event) => {
        setFuzzyTextInput(event.target.value);
    }

    const handleClearInput = (event) => {
        setClearTextInput(event.target.value);
    }

    const fuzzyResults = storyObjects.map((story) => {
        const relevance = StringSimilarity(fuzzyTextInput, (story.title+story.by));
        const storyObj = {name: story.title, author: story.by, time: story.time, url: story.url, relevance: relevance};
        return storyObj;
    })

    fuzzyResults.sort(
        (story1, story2) => 
        (story1.relevance < story2.relevance) ? 1 :
        (story1.relevance > story2.relevance) ? -1 : 0
    );

    const clearFilter = storyObjects.filter((story) => {
        return story.title.includes(clearTextInput)
    })

    const clearResults = clearFilter.map((story)=>{
        return {name: story.title, author: story.by, time: story.time, url: story.url, relevance: 1};
    })


    return(
        <div className="content">

            <input type="text" onChange={handleFuzzyInput} value={fuzzyTextInput} placeholder="fuzzy search"/>
            <StoryList stories = {fuzzyResults} filter={fuzzyTextInput}></StoryList>
            
            <input type="text" onChange={handleClearInput} value={clearTextInput} placeholder="clear search"/>
            <StoryList stories = {clearResults} filter={clearTextInput}></StoryList>
            
        </div>
    );

}

export default Container;