import './home.css'
import axios from 'axios';
import { useEffect, useState } from 'react';
export default function HomeBody(props:any) {

    let url = `${props.url}/index/`
    const [item, setItems] = useState<any[]>([])
    useEffect(()=>{
        axios.get(url)
        .then(res=>{
            setItems(res.data)
        })
        .catch(e=>{
            console.log(e)
        })
    },[url])
    
    function handleCardClick(input:any){
        props.setSongId(input.id)
        props.setAlbumArt(input.album_art)
        props.setAuthorName(input.author)
        props.setSongName(input.title)
        props.setSongUrl(input.music_file)
        props.setIsPlaying(true)
        props.setClickedSong(false)
        props.setClickedSong(true)
    }
    return (
        
        <>
            <section className="hero is-medium">
                <div className="hero-body">
                    {/* Will Add Feature tab later */}
                </div>
            </section>
            <section id="home_body" className="hero is-fullheight" >
                <div className="grid__container">
                    {item.map(items=>{
                        return(
                            <div className="grid__item" onClick={()=>handleCardClick(items)}>
                                <div className="card">
                                    <div className="card-image">
                                        <figure className="image is-square " >
                                        <img className="" src={`${props.url}/${items.album_art}`} alt="Placeholder_image" />
                                        </figure>
                                    </div>
                                    <div className="card-content">
                                        <div className="media">
                                        <div className="media-content">
                                            <p className="title is-4">{items.title}</p>
                                            <p className="subtitle is-6">{items.author}</p>
                                        </div>
                                        </div>

                                    </div>
                                    </div>
                            </div>
                        )
                    })}
                </div>
            </section>
        </>
        
    )
}
