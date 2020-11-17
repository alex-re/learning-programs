(function () {
    "use strict";
    var selectedIndex = document.getElementById('s-state').selectedIndex;
    var selectedValue = document.getElementById('s-state').option[selectedIndex].value;

    var state = document.getElementById('s-state');

    document.addEventListener('DOMContentLoaded', function () {

        document.getElementById('cart-hplus').addEventListener('submit', calTotal);


        var btn = document.getElementById('btn-estimate');
        btn.disabled = true;
        state.addEventListener('change', function () {

            // if(state.value==='')
            // {
            //     btn.disabled=true;
            // }
            // else{
            //     btn.disabled=false;
            // }

            // Shourt hand for upper codes.
            btn.disabled = (state.value === '');

        });

    });
    function calTotal(event) {
        event.preventDefault();

        var state = document.getElementById('s-state');
        if (state.value === '') {
            alert('please choose your shipping state.');
            state.focus();
        }
    }

})();
