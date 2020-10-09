document.addEventListener('DOMContentLoaded', function() {
 const btn = document.querySelector('.btn');
 const ani = new TextAnimate('.animate-title');
 ani.animate();
 btn.addEventListener('click', ani.animate.bind(ani));
});

class TextAnimate {
    constructor(el){
         this.el = document.querySelector(el);
         this.str = this.el.innerHTML.trim().split("");
         this.el.innerHTML = this._sptext();
    }
    _sptext() {
        return this.str.reduce((acc, curr) => {
            curr = curr.replace(/\s+/, '&nbsp;');
            return `${acc}<span class="char">${curr}</span>`;
        }, "");
    }
    animate() {
        this.el.classList.toggle('inview');
    }
}