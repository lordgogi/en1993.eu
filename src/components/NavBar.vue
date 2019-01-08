<template>
	<div class="nav-bar">
		<div class="logo"><router-link to="/">EN1993.eu</router-link></div>
		<span class="nav-link"><router-link to="/I_Shape">CROSS SECTION PROPERTIES</router-link></span>
		<span class="nav-link"><router-link to="/BoltInLine">BOLT IN-PLANE LOADING</router-link></span>
	</div>
</template>

<style scoped>

.logo {
	padding: 4px 16px;
	color: black;
	font-family: Metropolis Regular;
	font-size: 20px;
	font-weight: bold;
}

.logo a {
	color: black;
	text-decoration: none;
}

.nav-bar {
	background-color: #FFFFFF;
	color: #565656;
}

.nav-link {
		color: #565656;
}

.nav-link a {
	color: #565656;
	font-size: 14px;
	text-decoration: none;
	padding: 0px 16px;

}

.nav-link a:hover {
	background-color: gray;
	color: #FFFFFF;
	font-size: 14px;
	text-decoration: none;
	padding: 0px 16px;

}


</style>
