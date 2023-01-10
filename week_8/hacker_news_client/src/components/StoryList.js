import React from "react";
import StoryDetail from "./StoryDetail";

const StoryList = ({stories}) => {

    const storiesList = stories.map((story, index) => {
        return <StoryDetail story = {story} key={index}></StoryDetail>
    })

    return(
        <>
        <ul className="stories">
            {storiesList}
        </ul>
        </>
    );

}

export default StoryList;