document.querySelectorAll('.button').forEach(button => {
  let duration = 3000,
      svg = button.querySelector('svg'),
      svgPath = new Proxy({y: null, smoothing: null}, {
        set(target, key, value) {
          target[key] = value;
          if(target.y !== null && target.smoothing !== null) {
      svg.innerHTML = getPath(target.y, target.smoothing, null); }
          return true; },get(target, key) {
          return target [key];}});
  button.style.setProperty('--duration', duration);
  svgPath.y = 20;   svgPath.smoothing = 0;
  button.addEventListener('click', e => {
    e.preventDefault();
    if(!button.classList.contains('loading')) {
      button.classList.add('loading');
      gsap.to(svgPath, {
        smoothing: .3,
        duration: duration * .065 / 1000 });
      gsap.to(svgPath, {
        y: 12, 
        duration: duration .265 / 1000, 
        delay: duration .065 / 1000,
        ease: Elastic.easeOut.config(1.12, .4) });
