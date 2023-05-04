<template>
	<va-carousel
		v-model="value"
		:items="items"
		infinite
		indicators
		class="custom-carousel"
	/>
</template>
<script>
export default {
	data() {
		return {
			value: 0,
			items: [
				'https://salt.tikicdn.com/cache/w1080/ts/tka/d0/d6/7e/190525b538f71ad1cf8e7416f37caa17.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tikimsp/f7/f5/76/a26fca25991a5f86582aeaaade8fb23c.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tikimsp/27/17/d8/19949e0b41a2c244797bdc65ef2c27dc.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tikimsp/44/11/eb/733d4a7eb9de3d0768d862f8e611f76d.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tikimsp/d0/14/95/7ac13b0fa8644b52ccc12e8042a4798f.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tikimsp/17/8c/1e/ae4b0edf708c1872517324898036054b.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tikimsp/b0/1d/c3/b8385d7c3db040baf99597c2a01f4b9e.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tikimsp/9e/6d/2c/7989c7fc794294fc8c0fb3699650e149.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tikimsp/5a/1c/4a/e47adb885144e9127a68bb7c3e12f5d5.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tikimsp/75/e6/eb/9d53ed23fa43f20ba279adda4cad0d8d.png.webp',
				'https://salt.tikicdn.com/cache/w1080/ts/tka/d0/d6/7e/190525b538f71ad1cf8e7416f37caa17.png.webp'
			]
		}
	}
}
</script>
<style lang="scss" scoped>
.custom-carousel {
	height: 280px !important;
	width: 842px;
	border-radius: 8px;
	margin-right: 16px;
	cursor: pointer;
}
</style>
