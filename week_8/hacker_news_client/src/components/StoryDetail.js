import React from "react";

const StoryDetail = ({story, index}) => {

    const date = new Date(story.time*1000); 
    
    const formattedDate = `${date.getDate()}/${date.getMonth()+1}/${date.getFullYear()}`

    
    console.log(story.relevance);


    return(
        <>
        {story.relevance > 0.15 ? <div className="story-container" id={index}>
            {story.url ? <h3><a href={story.url}>{story.name}</a></h3> : <h3>{story.name}</h3>}

            <li>{story.author}</li>
            <li>{formattedDate}</li>
        </div>
        :
        <div className="story-minimised" id={index}>
            {story.url ? <h3><a href={story.url}>{story.name}</a></h3> : <h3>{story.name}</h3>}
        </div>
        }
        
        </>
    )

}

export default StoryDetail;