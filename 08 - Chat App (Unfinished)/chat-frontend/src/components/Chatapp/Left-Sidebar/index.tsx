import "./left-sidebar.sass"

const LeftAside = () => {
    return (
        <section className="hero is-fullheight-with-navbar left-menu-fullheight">
            <aside className="menu">
                {/* For Loop starts here */}
                <article className="media ">
                    <figure className="media-left">
                        <p className="image is-64x64">
                            <img className="is-rounded" alt="user"
                                 src="https://bulma.io/images/placeholders/128x128.png"/>
                        </p>
                    </figure>
                    <div className="media-content">
                        <div className="content">
                            <p>
                                <span>John Smith</span>
                                <br/>
                                <div className="reply">
                                    You: Hello World
                                </div>
                            </p>
                        </div>
                    </div>
                </article>
                <hr/>
            </aside>
        </section>
    )
}
export default LeftAside
