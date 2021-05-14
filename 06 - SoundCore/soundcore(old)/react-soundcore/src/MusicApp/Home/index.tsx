

import { useState } from "react";
import HomeBody from "./HomeBody/HomeBody";
import MusicFooter from "./MusicFooter/MusicFooter";
import SideNav from "./SideNav/SideNav";

export default function MusicHome(props:any) {
  const [albumArt, setAlbumArt] = useState("");
  const [songName, setSongName] = useState("");
  const [authorName,setAuthorName] = useState(""); 
  const [songUrl, setSongUrl] = useState('');
  const [clickedSong,setClickedSong] = useState(false);
  const [songId,setSongId] = useState('');
  const [isPlayingAudio, setIsPlaying] = useState(false)
  
  return (
    <>
      <SideNav />
      <HomeBody setIsPlaying={setIsPlaying} setSongId={setSongId} setClickedSong={setClickedSong} setSongName={setSongName} setSongUrl={setSongUrl} setAuthorName={setAuthorName} setAlbumArt={setAlbumArt} url={props.url}/>
      <MusicFooter isPlayingAudio={isPlayingAudio} setIsPlaying={setIsPlaying} url={props.url} songId={songId} clickedSong={clickedSong} author_name={authorName} song_name={songName} song_url={songUrl} album_art={albumArt}/>
    </>
  )
}