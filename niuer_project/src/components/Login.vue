<template>
  <section>
    <div class="color"></div>
    <div class="color"></div>
    <div class="color"></div>
    <div class="box">
      <div class="square"></div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="container">
        <div class="form">
          <h2>个人博客</h2>
          <form>
            <div class="inputBox">
              <input type="text" placeholder="用户名" v-model="loginForm.uid" />
            </div>
            <div class="inputBox">
              <input type="password" placeholder="密码" v-model="loginForm.pwd" />
            </div>
            <div class="inputBox">
              <input type="submit" value="登录" @click="login" />
            </div>
            <p class="forget">
              忘记密码 ?
              <a href="#">找回密码</a>
            </p>
            <p class="forget">
              还没有账号 ?
              <span @click="register">注册</span>
            </p>
          </form>
        </div>
      </div>
    </div>

    <!-- 注册 -->
    <div class="box1">
      <div class="square"></div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="container">
        <div class="form clearfix">
          <h2>注册</h2>
          <form>
            <div class="inputBox">
              <input type="text" placeholder="输入用户名" v-model="registerForm.uid" />
            </div>
            <div class="inputBox">
              <input type="password" placeholder="输入密码" v-model="registerForm.pwd" />
            </div>
            <div class="inputBox">
              <input type="password" placeholder="确定密码" v-model="registerForm.repwd" />
            </div>
            <!-- 后面可以增加手机号码验证 -->
            <div class="inputBox fl">
              <input type="submit" value="返回登录" @click="register" />
            </div>
            <div class="inputBox fl">
              <input type="submit" value="注册" @click="inforegister" class="fr" />
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      // 这是登入表单的数据绑定对象
      loginForm: {
        uid: "",
        pwd: "",
      },
      registerForm: {
        uid: "",
        pwd: "",
        repwd: "",
      },
      isnologin: "false",
    };
  },
  mounted() {
    this.createcode();
  },
  methods: {
    //页面加载时运行的函数
    createcode() {
      document.querySelector(".box1").style.visibility = "hidden";
      document.querySelector(".box").style.visibility = "visible";
    },
    // 点击登录按钮，进行数据验证
    login() {
      if (this.loginForm.uid == "") {
        this.$message.error("用户名不为空");
        return;
      }
      if (this.loginForm.pwd == "") {
        this.$message.error("密码不为空");
        return;
      }
      // 判定账号密码是否含有中文
      if (/.*[\u4e00-\u9fa5]+.*$/.test(this.loginForm.uid) || /.*[\u4e00-\u9fa5]+.*$/.test(this.loginForm.pwd)) {
        this.$message.error("用户名或密码不能含中文");
        return;
      }
      this.$http
        .post(this.API.API_Login, {
          data: this.loginForm,
        })
        .then((res) => {
          if (res.data.code === 200) {
            //验证成功
            this.$message({
              message: "登录成功",
              type: "success",
            });
            //路由跳转
          } else {
            this.$message.error("用户名或密码不正确");
          }
        });
    },
    register() {
      console.log("test");
      var box1 = document.querySelector(".box1");
      var box = document.querySelector(".box");
      box1.className = "box";
      box.className = "box1";
      this.createcode();
    },
    // 点击注册按钮，验证注册信息
    inforegister() {
      console.log("确定注册");
      if (this.registerForm.uid == "") {
        this.$message.error("用户名不为空");
        return;
      }
      if (this.registerForm.pwd == "") {
        this.$message.error("密码不为空");
        return;
      }
      if (this.registerForm.repwd == "") {
        this.$message.error("确定密码不为空");
        return;
      }
      if (this.registerForm.repwd != this.registerForm.pwd) {
        this.$message.error("两次密码不一致")
        return;
      }
      if (/.*[\u4e00-\u9fa5]+.*$/.test(this.registerForm.uid) || /.*[\u4e00-\u9fa5]+.*$/.test(this.registerForm.pwd)) {
        this.$message.error("用户名或密码不能含中文");
        return;
      }
      if (this.registerForm.uid.length < 6 || this.registerForm.uid.length > 11) {
        this.$message.error("用户名长度范围为6~11");
        return;
      }
      if (this.registerForm.pwd.length < 8 || this.registerForm.pwd.length > 16) {
        this.$message.error("密码长度范围为8~16");
        return;
      }
      this.$http
        .post(this.API.API_Login, {
          data: this.registerForm,
        })
        .then((res) => {
          if (res.data.code === 200) {
            //验证成功
            this.$message({
              message: "注册成功",
              type: "success",
            });
            //路由跳转
            this.register();
          } else {
            this.$message.error("该用户名已经存在");
          }
        });
    },
  },
};
</script>

<style lang="less" scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
/* 背景图 */
section {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to bottom, #f1f4f9, #dff1ff);
}
section .color {
  position: absolute;
  filter: blur(150px);
}
section .color:nth-child(1) {
  top: -350px;
  width: 600px;
  height: 600px;
  background: #ff359b;
}
section .color:nth-child(2) {
  bottom: -150px;
  left: 100px;
  width: 500px;
  height: 500px;
  background: #fffd87;
}

section .color:nth-child(3) {
  bottom: 50px;
  right: 100px;
  width: 300px;
  height: 300px;
  background: #00d2ff;
}

/* 登录框 */
.box {
  position: relative;
}
.box .square {
  position: absolute;
  backdrop-filter: blur(5px);
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-right: 1px solid rgba(255, 255, 255, 0.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  animation: animate 10s linear infinite;
}
@keyframes animate {
  0%,
  100% {
    transform: translateY(-40px);
  }
  50% {
    transform: translateY(40px);
  }
}
.box .square:nth-child(1) {
  top: -50px;
  right: -60px;
  width: 100px;
  height: 100px;
}
.box .square:nth-child(2) {
  top: 150px;
  left: -100px;
  width: 120px;
  height: 120px;
  z-index: 2;
}
.box .square:nth-child(3) {
  bottom: 50px;
  right: -60px;
  width: 80px;
  height: 80px;
  z-index: 2;
}
.box .square:nth-child(4) {
  bottom: -80px;
  left: 100px;
  width: 50px;
  height: 50px;
}
.box .square:nth-child(5) {
  top: -80px;
  left: 100px;
  width: 60px;
  height: 60px;
}

.box .container {
  position: relative;
  width: 400px;
  min-height: 400px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  backdrop-filter: blur(5px);
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-right: 1px solid rgba(255, 255, 255, 0.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}
.box .form {
  position: relative;
  width: 100%;
  height: 100%;
  padding: 40px;
}
.box .form h2 {
  position: relative;
  color: #fff;
  font-size: 24px;
  font-weight: 600;
  letter-spacing: 1px;
  margin-bottom: 40px;
}
.box .form h2::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: -10px;
  width: 80px;
  height: 4px;
  background: #fff;
}
.box .form .inputBox {
  width: 100%;
  margin-top: 20px;
}
.box .form .fl {
  width: 50%;
}
.box .form .inputBox input {
  width: 100%;
  background: rgba(255, 255, 255, 0.2);
  border: none;
  outline: none;
  padding: 10px 20px;
  border-radius: 35px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-right: 1px solid rgba(255, 255, 255, 0.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 16px;
  letter-spacing: 1px;
  color: #fff;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}
.box .form .inputBox input::placeholder {
  color: #fff;
}
.box .form .inputBox input[type="submit"] {
  background: #fff;
  color: #666;
  max-width: 100px;
  cursor: pointer;
  margin-bottom: 20px;
  font-weight: 600;
}
.box .forget {
  margin-top: 5px;
  color: #fff;
}
.box .forget span {
  color: #fff;
  font-weight: 600;
  text-decoration: underline;
  cursor: pointer;
}
.box .forget a {
  color: #fff;
  font-weight: 600;
}
.box1 {
  position: fixed;
}
</style>
