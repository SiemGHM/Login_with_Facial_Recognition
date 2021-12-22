$(document).ready(function(){
    let namespace = "/test";
    let video = document.querySelector("#videoElement");
    let canvas = document.querySelector("#canvasElement");
    let ctx = canvas.getContext('2d');
    photo = document.getElementById('photo');
    var localMediaStream = null;
  
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    socket.on('redirect', function (data) {
      console.log('siemsiemsiem')
      window.location = data.url;
    });
  
    function sendSnapshot() {
      if (!localMediaStream) {
        return;
      }
  
      ctx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight, 0, 0, 300, 150);
  
      let dataURL = canvas.toDataURL('image/jpeg');
      socket.emit('input image', dataURL);
  
      socket.emit('output image')
  
      var img = new Image();
      socket.on('out-image-event',function(data){
  
  
      img.src = dataURL//data.image_data
      photo.setAttribute('src', data.image_data);
      console.log('if i')
  
      });
  
  
    }
  
    socket.on('connect', function() {
      console.log('Connected!');
    });



    
   

    var constraints = {
      video: {
        width: { min: 640 },
        height: { min: 480 }
      }
    };
  
    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
      video.srcObject = stream;
      localMediaStream = stream;
  
      setInterval(function () {
        sendSnapshot();
      }, 50);
    }).catch(function(error) {
      console.log(error);
    });
  });








  