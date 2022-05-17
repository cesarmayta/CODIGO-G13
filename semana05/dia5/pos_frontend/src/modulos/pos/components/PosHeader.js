import React from 'react';
import { Link } from 'react-router-dom';

// import miImagen from './../../../assets/images/achirvo.svg';

const PosHeader = () => {
	return (
		<header className="header">
			<div className="header__logo">
				{/* <img src={miImagen} alt="" /> */}
				<img src="/images/logo.svg" alt="" />
			</div>
			<div className="header__buscador">
				<img src="/images/search.svg" alt="" />
				<input
					type="text"
					className="header__input"
					placeholder="Busca un término"
				/>
			</div>
			<div className="header__usuario">
				<Link to="/admin/dashboard" className="btn btn-success">
					Ir a Dashboard
				</Link>
				<img src="https://randomuser.me/api/portraits/men/90.jpg" alt="" />
				<span>Jorge Garnica</span>
			</div>
		</header>
	);
};

export default PosHeader;
