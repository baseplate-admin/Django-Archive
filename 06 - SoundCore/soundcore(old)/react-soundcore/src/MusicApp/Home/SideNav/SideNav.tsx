import HomeIcon from './Icons/home'
import LibraryIcon from './Icons/library'
import SearchIcon from './Icons/search'
import './sidebar.css'

export default function SideNav() {

    let color = "#969696"
    return (
        <aside className="menu full__height">
            <p className="menu-label">
                Logo Here
            </p>
            <ul className="menu-list">
                <ul className="svg__icons">
                    <li ><HomeIcon height={22} width={22} color={color} /></li>
                    <li ><SearchIcon height={22} width={22} color={color} /></li>
                    <li ><LibraryIcon height={20} width={20} color={color} /></li>
                </ul>
                <li className={'active'} >Home</li>
                <li >Search</li>
                <li >Library</li>
            </ul>
        </aside>
    )
}