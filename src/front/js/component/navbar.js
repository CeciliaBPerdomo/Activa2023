import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<div className="principal" style={{marginBottom: "25px"}}>
		<nav className="navbar navbar-light bg-light" >
			<div className="container">
				{/* <Link to="/"> */}
					<span className="navbar-brand mb-0 h1" style={{color: "black"}}>
						<b>
						Activa Fitness Club
						</b>
					</span>
				{/* </Link> */}
				<div className="ml-auto">
					<Link to="/demo">
						{/* <button className="btn btn-primary">Check the Context in action</button> */}
					</Link>
				</div>
			</div>
		</nav>
		</div>
	);
};
