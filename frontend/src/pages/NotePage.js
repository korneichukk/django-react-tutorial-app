import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

const NotePage = () => {
    let noteID = useParams().id;
    let [note, setNote] = useState();

    useEffect(() => {
        getNote();
    }, [noteID]);

    let getNote = async () => {
        let response = await fetch(`http://localhost:8000/api/note/${noteID}`)
        let data = await response.json()
        setNote(data)
    }

    return (
        <div>
            <p>{note?.body}</p>
        </div>
    )
}

export default NotePage