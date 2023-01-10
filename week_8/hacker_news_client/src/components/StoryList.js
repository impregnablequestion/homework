import React from "react";
import StoryDetail from "./StoryDetail";

const StoryList = ({stories, filter}) => {

    const storiesList = stories.map((story, index) => {
        return <StoryDetail story = {story} key={index} filter={filter}></StoryDetail>
    })

    return(
        <>
        <ul>
            {storiesList}
        </ul>
        </>
    );

}

export default StoryList;