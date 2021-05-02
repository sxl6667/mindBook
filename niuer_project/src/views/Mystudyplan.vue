<template>
  <div class="container clearfix">
    <header>
      <Click class="fl click"></Click>
    </header>
    <aside class="fl">
        <el-menu
          :default-active="$route.path"
          :collapse="isCollapse"
          router
          overflow-y:
          scroll
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose">
        <el-menu-item index="/blog/StudyPlan">
          <i class="fa fa-map-o" aria- hidden="true"></i>
          <span slot="title">学习计划</span>
        </el-menu-item>
        <el-menu-item index="/blog/Idea">
          <i class="fa fa-lightbulb-o" aria- hidden="true"></i>
          <span slot="title">想法</span>
        </el-menu-item>
        <el-menu-item index="/blog/Navigation">
          <i class="fa fa-paper-plane-o" aria- hidden="true"></i>
          <span slot="title">导航</span>
        </el-menu-item>
        <el-menu-item index="/blog/Case">
          <i class="fa fa-newspaper-o" aria- hidden="true"></i>
          <span slot="title">案例</span>
        </el-menu-item>
        <el-menu-item index="/blog/Photo">
          <i class="fa fa-picture-o" aria- hidden="true"></i>
          <span slot="title">相册</span>
        </el-menu-item>
        <el-menu-item index="/blog/StudyMaterials">
          <i class="fa fa-university" aria- hidden="true"></i >
          <span slot="title">学习资源</span>
        </el-menu-item>
        <el-menu-item index="/blog/Api">
          <i class="fa fa-share-alt-square" aria-hidden="true"></i>
          <span slot="title">API</span>
        </el-menu-item>
      </el-menu>
    </aside>
    <main class="fr"><router-view></router-view></main>
    <footer class="fr"></footer>
  </div>
</template>
<script>
import Click from "../components/Click";
import '../lib/font-awesome/css/font-awesome.min.css'
import '../common/font.css'
export default {
  name: "Mystudyplan",
  components: {
    Click,
  },
  data() {
    return {
      windowWidth: document.documentElement.clientWidth, //实时屏幕宽度
      isCollapse:'',
    };
  },
  created(){
    if(this.windowWidth<=640){
      this.isCollapse = true
    }
    if(this.windowWidth >640){
      this.isCollapse = false
    }
  },
  mounted(){
    let that = this;
    window.onresize = () => {
    return (() => {
    window.fullHeight = document.documentElement.clientHeight;
    window.fullWidth = document.documentElement.clientWidth;
    that.windowWidth = window.fullWidth; // 宽
    })()
    };
  },
  watch:{
    windowWidth(newName, oldName){
      console.log(this.windowWidth)
      if(this.windowWidth<=640){
        this.isCollapse = true
      }
      if(this.windowWidth >640){
        this.isCollapse = false
      }
    }
  }
};
</script>
<style lang="less" scoped>
.container {
  // min-height: 100%;
//   height: 1000px;
  background: rgb(216, 17, 133);
  position: relative;
  header {
    height: 180px;
    width: 100%;
    background: rgb(119, 78, 78);
    position: fixed;
  }
  aside {
    position: fixed;
    top: 180px;
    height: 100%;
    width: 20%;
    background: white;
    z-index: 10;
    font-family: "stx";
    letter-spacing:10px; //字体间隔
  }
  .fa{
    text-align: center;
  }
  .el-menu-vertical-demo{
    height: 760px;
    width: 100%;
    min-width: 64px;
  }
  main {
    margin-top: 180px;
    width: 80%;
    min-width: 326px;
    background: rgb(171, 171, 230);
    height: 620px;
  }
  footer {
    height: 100px;
    width: 80%;
    background: rgb(56, 56, 92);
  }
}
</style>