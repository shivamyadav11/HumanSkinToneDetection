var url = "";
var constraints = { video: { facingMode: "user" }, audio: false };
const cameraView = document.querySelector("#camera--view"),
  cameraOutput = document.querySelector("#camera--output"),
  cameraSensor = document.querySelector("#camera--sensor"),
  cameraTrigger = document.querySelector("#camera--trigger"),
  cameraStop = document.querySelector("#camera--stop"),
  cameraSubmit = document.querySelector("#camera--submit");
function cameraStart() {
  navigator.mediaDevices
    .getUserMedia(constraints)
    .then(function (stream) {
      track = stream.getTracks()[0];
      cameraView.srcObject = stream;
    })
    .catch(function (error) {
      console.error("Oops. Something is broken.", error);
    });
}
cameraTrigger.onclick = function () {
  cameraSensor.width = cameraView.videoWidth;
  cameraSensor.height = cameraView.videoHeight;
  cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
  cameraOutput.src = cameraSensor.toDataURL("image/webp");
  url = cameraOutput.src;
  cameraOutput.classList.add("taken");
};
cameraStop.onclick = function () {
  // document.querySelector("#image").setAttribute("value", url);
  window.location.href = "/";
};
cameraSubmit.onclick = function () {
  document.querySelector("#image").setAttribute("value", url);
  // window.location.href = "/";
};
window.addEventListener("load", cameraStart, false);
