$(document).ready(function () {
    document.documentElement.style.fontSize = innerWidth/10+"px";   // 设置页面字体大小是 宽度的1/10

    var n=1;
    $tt1 = $(".myul:eq(0)");
    $tt1.css("display","block");

    $(".bott").bind("click",function () {
        $tt = $(".myul:eq("+n+")");
        $tt.css("display","block");
        // console.log($tt)
        if(n<26){
            n++;
        }
        else{
            var $jsp = $("<div style='width: 100%; height: 1.3rem; line-height:1.3rem;text-align:center;font-size: 0.7rem; color:rgba(50,50,255,0.5); position: fixed; z-index: 10;left: 0;bottom:5rem;'>@j@已经最后一步了~~~</div>");
            $("body").prepend($jsp);
            setTimeout(function () {
                var $rejsp = $("body div:first");
                $rejsp.remove()
            },2000)
        }
        // $(this).css("color","#29f0f6");
        // $(this).css("cursor","pointer");
    });

});