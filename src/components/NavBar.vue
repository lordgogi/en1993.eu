<template>
	<div class="nav-bar">
		<span class="nav-link"><router-link to="/">Home</router-link></span>
		<span class="nav-link"><router-link to="/CrossSections">Cross Sections</router-link></span>
		<span class="nav-link"><router-link to="/About">About</router-link></span>
	</div>
</template>

<style scoped>

.nav-bar {
	background-color: #FFFFFF;
	color: #FFFFFF;
	height: 40px;
}

.nav-link {
		color: #FFFFFF;
}

.nav-link a {
	color: #FFFFFF;
	text-decoration: none;
	padding: 8px 16px;
}


</style>
