import React from "react";

const StoryDetail = ({story, filter}) => {

    // const title = story.title

    console.log(filter);

    return(
        <p>{story.title}</p>
    );

}

export default StoryDetail;