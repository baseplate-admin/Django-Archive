import './upper-navbar.sass'

const UpperNavbar = () => {
    return(
    <nav className="navbar is-fixed-top">
        <div className="columns upper-navbar is-mobile">
            <div className="column">
                First column
            </div>
            <div className="column">
                Second column
            </div>
            <div className="column">
                Third column
            </div>
            <div className="column">
                Fourth column
            </div>
        </div>
    </nav>
    )
}
export default UpperNavbar;