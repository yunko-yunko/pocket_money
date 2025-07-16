document.addEventListener("DOMContentLoaded", function() {

  const registerForm = document.getElementById("register-form");
  if (registerForm) {
    registerForm.addEventListener("submit", async function(event) {
      event.preventDefault(); // 폼 제출시 페이지 리로드 방지
      const username = document.getElementById("reg-username").value;
      const password = document.getElementById("reg-password").value;

      try {
        const response = await fetch("/auth/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        if (response.ok) {
          alert("회원가입 성공!");
          console.log("가입된 사용자:", data);
        } else {
          alert("회원가입 실패: " + data.detail);
        }
      } catch (error) {
        console.error("Error during registration:", error);
      }
    });
  }
  
  const loginForm = document.getElementById("login-form");
  if (loginForm) {
    loginForm.addEventListener("submit", async function(e) {
      e.preventDefault();  // 폼 제출 시 페이지 리로드 방지
      const username = document.getElementById("login-username").value;
      const password = document.getElementById("login-password").value;
  
      try {
        const response = await fetch("/auth/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ username, password })
        });
  
        const data = await response.json();
        if (response.ok) {
          // localStorage에 사용자 id를 저장
          localStorage.setItem("user_id", data.id);
          // 로그인 성공 후, 해당 사용자의 용돈 내역 페이지로 이동
          window.location.href = "/expenses?user_id=" + data.id;
        } else {
          alert("로그인 실패: " + data.detail);
        }
      } catch (err) {
        console.error("로그인 도중 오류 발생:", err);
        alert("로그인 중 오류가 발생했습니다. 다시 시도해주세요.");
      }
    });
  }

});