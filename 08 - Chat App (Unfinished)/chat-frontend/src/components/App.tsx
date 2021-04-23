import "./app.sass"
// Responsive Sass 
// responsive-mobile.sass contains media query for android till ( 768px )
import "./responsive-mobile.sass"
// responsive-tablet.sass contains media query for ipad till ( 900px )
import "./responsive-tablet.sass"

// Import all the components

import LeftAside from "./Left-Sidebar";
import RightAside from "./RIght-Sidebar";
import MiddleColumn from "./Middle-Menu";
import UpperNavbar from "./Upper-Navbar";

function App() {
  return (
    <>
      <div className="main-column-wrapper">
        <UpperNavbar />
        <div className="columns main-column is-mobile">
          <div className="column is-one-fifth" id="left-menu">
            <LeftAside
            />
          </div>

          <div className="column" id="middle-menu">
            <MiddleColumn />
          </div>

          <div className="column is-one-quarter " id="right-menu">
            <RightAside />
          </div>

        </div>
      </div>

    </>
  );
}

export default App;
