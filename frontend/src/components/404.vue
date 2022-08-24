<template>
    <h4 id="not-found-message">
        (๑<span id="first-paw">و</span>•̀ω•́)<span id="second-paw">و</span> Not found ...
    </h4>

</template>

<style type="text/css">

@keyframes slidein {
  from {
    top: 0.3rem;
  }

  50% {
    top: -0.3rem;
  }

  to {
    top: 0.3rem;
  }
}

#first-paw, #second-paw {
    animation-name: slidein;
    animation-duration: 1.2s;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
}

#second-paw {
    animation-direction: reverse;
}


</style>