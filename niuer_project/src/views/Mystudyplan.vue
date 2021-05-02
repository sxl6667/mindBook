<template>
  <div class="container clearfix">
    <header class="clearfix">
      <div style="width:20%;height:100%" class="fl"></div>
      <Click class="fl"></Click>
    </header>
    <aside class="fl"></aside>
    <main class="fr"></main>
    <footer class="fr"></footer>
  </div>
</template>
<script>
import Click from "../components/Click";
export default {
  name: "Mystudyplan",
  components: {
    Click,
  },
  data() {
    return {};
  },
};
</script>
<style lang="less" scoped>
.container {
  // min-height: 100%;
//   height: 1000px;
  background: rgb(216, 17, 133);
  position: relative;
  header {
    height: 100px;
    width: 100%;
    background: rgb(119, 78, 78);
    position: fixed;
  }
  aside {
    position: fixed;
    height: 100%;
    width: 20%;
    background: rgb(47, 83, 65);
    z-index: 10;
  }
  main {
    margin-top: 100px;
    width: 80%;
    background: rgb(171, 171, 230);
    height: 700px;
  }
  footer {
    height: 100px;
    width: 80%;
    background: rgb(56, 56, 92);
  }
}
</style>