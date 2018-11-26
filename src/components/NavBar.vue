<template>
	<div class="nav-bar">
		<span class="nav-link"><router-link to="/">Home</router-link></span>
		<span class="nav-link"><router-link to="/I_Shape">Cross Sections</router-link></span>
		<span class="nav-link"><router-link to="/BoltInLine">Bolt In-line Loading</router-link></span>
	</div>
</template>

<style scoped>

.nav-bar {
	background-color: #FFFFFF;
	color: #565656;
	height: 40px;
}

.nav-link {
		color: #565656;
}

.nav-link a {
	color: #565656;
	text-decoration: none;
	padding: 8px 16px;
}


</style>
