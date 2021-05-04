import UpperNavbar from "./Upper-Navbar";
import MiddleMenu from "./Middle-Menu";

const App = (props: any) => {
    return (
        <>
            <UpperNavbar/>
            <MiddleMenu setJwt={props.setJwt} />
        </>
    )
}
export default App