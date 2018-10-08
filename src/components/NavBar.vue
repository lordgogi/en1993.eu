<template>
	<div class="nav-bar">
		<div class="wrapper">
			<ul>
				<li><router-link to="/Home">Home</router-link></li>
				<li><router-link to="/crosssections">Cross Sections</router-link></li>
				<li><router-link to="/About">About</router-link></li>
			</ul>
		</div>
	</div>
</template>

<style scoped>

.nav-bar {
	text-align: left;
	padding: 0 0;
	background-color: #584b4f;
	color: #efeae1;
	font-size: 14px;

}

.wrapper {
	width: 860px;
	margin: 0 auto;
}

ul {
	list-style-type: none;
	margin: 0;
	padding: 0;
	overflow: hidden;
}

li{
	display: inline-block;
}

li a {
	display: block;
	color: #EFEAE1;
	text-align: center;
	padding: 8px 16px;
	text-decoration: none;
}

li a:hover {
	background-color: #111;
}

</style>
