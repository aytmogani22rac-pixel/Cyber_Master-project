      let step = 1;
      let currentMode = "";

      function toggleSide() {
        document.getElementById("side").classList.toggle("active");
      }

      function tiltCard(e, card) {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const rotateX = (rect.height / 2 - y) / 10;
        const rotateY = (x - rect.width / 2) / 10;
        card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
      }
      function resetTilt(card) {
        card.style.transform = `rotateX(0deg) rotateY(0deg) scale(1)`;
      }

      function goHome() {
        step = 1;
        document.getElementById("s1").style.display = "block";
        document.getElementById("s2").style.display = "none";
        document.getElementById("s3").style.display = "none";
        document.getElementById("back").style.display = "none";
        toggleSide();
      }

      function addToFileHistory(filePath) {
        const history = document.getElementById("fileLog");
        if (history.innerHTML.includes("Your history is empty"))
          history.innerHTML = "";
        const time = new Date().toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        });
        history.innerHTML =
          `<div class="file-item"><span style="color:#555">[${time}]</span> ${filePath}</div>` +
          history.innerHTML;
      }

      function toS2() {
        if (!document.getElementById("user").value) {
          alert("Please enter your name.");
          return;
        }
        if (!document.getElementById("check").checked) {
          alert("You must agree to the terms.");
          return;
        }
        step = 2;
        document.getElementById("s1").style.display = "none";
        document.getElementById("s2").style.display = "grid";
        document.getElementById("back").style.display = "block";
      }

      function toS3(m) {
        step = 3;
        currentMode = m;
        document.getElementById("targetLabel").innerText =
          m === "extract" ? "FILE TARGET:" : "INTEGRITY TARGET:";
        document.getElementById("s2").style.display = "none";
        document.getElementById("s3").style.display = "block";
      }

      function goBack() {
        if (step === 2) {
          step = 1;
          document.getElementById("s2").style.display = "none";
          document.getElementById("s1").style.display = "block";
          document.getElementById("back").style.display = "none";
        } else if (step === 3) {
          step = 2;
          document.getElementById("s3").style.display = "none";
          document.getElementById("s2").style.display = "grid";
        }
      }

      async function finalRun() {
        const p1 = document.getElementById("path1").value;
        if (p1) {
          addToFileHistory(p1);
          let result = await eel.process_request(
            p1,
            currentMode,
            document.getElementById("path2").value,
          )();

          // إظهار النتيجة في المودال بدلاً من الـ alert
          showModal(result);
        }
      }

      function showModal(msg) {
        document.getElementById("modalMessage").innerText = msg;
        document.getElementById("resultModal").style.display = "block";
      }

      function closeModal() {
        document.getElementById("resultModal").style.display = "none";
      }

      function revealNext() {
        if (
          document.getElementById("path1").value.length > 2 &&
          currentMode === "crack"
        )
          document.getElementById("extraField").style.display = "block";
      }

      async function openBrowser(id) {
        let path = await eel.open_file_dialog()();
        if (path) {
          document.getElementById(id).value = path;
          if (id === "path1") revealNext();
        }
      }