/* ═══════════════════════════════════════════════════════════
   LeadFlow Premium — Three.js 3D Background
   ═══════════════════════════════════════════════════════════ */
(function(){
  if(typeof THREE==='undefined') return;
  var canvas=document.getElementById('threeBg');
  if(!canvas) return;
  var scene=new THREE.Scene();
  var camera=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
  var renderer=new THREE.WebGLRenderer({canvas:canvas,alpha:true,antialias:true});
  renderer.setSize(window.innerWidth,window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
  renderer.setClearColor(0x000000,0);

  /* Floating geometric shapes */
  var geometries=[];
  var materials=[
    new THREE.MeshPhongMaterial({color:0x00ffaa,transparent:true,opacity:0.12,wireframe:true}),
    new THREE.MeshPhongMaterial({color:0x00ccff,transparent:true,opacity:0.1,wireframe:true}),
    new THREE.MeshPhongMaterial({color:0xff00aa,transparent:true,opacity:0.08,wireframe:true}),
    new THREE.MeshPhongMaterial({color:0xffaa00,transparent:true,opacity:0.1,wireframe:true})
  ];
  var shapes=[
    new THREE.IcosahedronGeometry(1.5,0),
    new THREE.OctahedronGeometry(1.2,0),
    new THREE.TorusGeometry(1,0.3,8,16),
    new THREE.TetrahedronGeometry(1.3,0),
    new THREE.DodecahedronGeometry(1,0),
    new THREE.TorusKnotGeometry(0.8,0.2,64,8)
  ];

  for(var i=0;i<12;i++){
    var geo=shapes[i%shapes.length];
    var mat=materials[i%materials.length].clone();
    mat.opacity=0.04+Math.random()*0.08;
    var mesh=new THREE.Mesh(geo,mat);
    mesh.position.set((Math.random()-0.5)*20,(Math.random()-0.5)*12,(Math.random()-0.5)*10);
    mesh.rotation.set(Math.random()*Math.PI,Math.random()*Math.PI,Math.random()*Math.PI);
    mesh.userData={
      rotSpeed:{x:(Math.random()-0.5)*0.005,y:(Math.random()-0.5)*0.005,z:(Math.random()-0.5)*0.003},
      floatSpeed:0.3+Math.random()*0.5,
      floatAmp:0.3+Math.random()*0.5,
      baseY:mesh.position.y
    };
    scene.add(mesh);
    geometries.push(mesh);
  }

  /* Particle system */
  var particleCount=200;
  var pGeo=new THREE.BufferGeometry();
  var positions=new Float32Array(particleCount*3);
  var colors=new Float32Array(particleCount*3);
  var accent=new THREE.Color(0x00ffaa);
  for(var i=0;i<particleCount;i++){
    positions[i*3]=(Math.random()-0.5)*30;
    positions[i*3+1]=(Math.random()-0.5)*20;
    positions[i*3+2]=(Math.random()-0.5)*15;
    var c=accent.clone();
    c.offsetHSL(Math.random()*0.3-0.15,0,0);
    colors[i*3]=c.r;colors[i*3+1]=c.g;colors[i*3+2]=c.b;
  }
  pGeo.setAttribute('position',new THREE.BufferAttribute(positions,3));
  pGeo.setAttribute('color',new THREE.BufferAttribute(colors,3));
  var pMat=new THREE.PointsMaterial({size:0.04,vertexColors:true,transparent:true,opacity:0.6,blending:THREE.AdditiveBlending});
  var particles=new THREE.Points(pGeo,pMat);
  scene.add(particles);

  /* Lights */
  scene.add(new THREE.AmbientLight(0x404060,0.5));
  var light1=new THREE.PointLight(0x00ffaa,1,30);
  light1.position.set(5,5,5);
  scene.add(light1);
  var light2=new THREE.PointLight(0x0066ff,0.6,25);
  light2.position.set(-5,-3,3);
  scene.add(light2);

  camera.position.z=8;

  /* Mouse interaction */
  var mouse={x:0,y:0};
  document.addEventListener('mousemove',function(e){
    mouse.x=(e.clientX/window.innerWidth)*2-1;
    mouse.y=-(e.clientY/window.innerHeight)*2+1;
  });

  var time=0;
  function animate(){
    requestAnimationFrame(animate);
    time+=0.01;
    geometries.forEach(function(mesh){
      mesh.rotation.x+=mesh.userData.rotSpeed.x;
      mesh.rotation.y+=mesh.userData.rotSpeed.y;
      mesh.rotation.z+=mesh.userData.rotSpeed.z;
      mesh.position.y=mesh.userData.baseY+Math.sin(time*mesh.userData.floatSpeed)*mesh.userData.floatAmp;
    });
    particles.rotation.y+=0.0003;
    particles.rotation.x+=0.0001;
    camera.position.x+=(mouse.x*1.5-camera.position.x)*0.02;
    camera.position.y+=(mouse.y*1-camera.position.y)*0.02;
    camera.lookAt(scene.position);
    light1.position.x=Math.sin(time*0.5)*5;
    light1.position.z=Math.cos(time*0.5)*5;
    renderer.render(scene,camera);
  }
  animate();

  window.addEventListener('resize',function(){
    camera.aspect=window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth,window.innerHeight);
  });
})();
