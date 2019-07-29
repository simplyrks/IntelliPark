$(function() {
    let floorNo = 1;

    let map1 = $("#map1");
    let map2 = $("#map2");
    let map3 = $("#map3");

    init();

    function init() {
        if (window.location.href.indexOf("floor") !== -1) {
            floorNo = parseInt(window.location.href.split("=")[1])
        }

        openMap(floorNo);
        getReq(floorNo);
    }

    function showMap(data, fno) {
        $(`#map${fno}`).html(`<h2 class="map" >Map ${fno}</h2>`);

        for(let i = 0; i<data.length; i+=4) {
            $(`#map${fno}`).append(
                `<div class="row">
                    <div class="${ data[i].id ? 'filled': 'empty'} cars">
                        ${data[i].id || "Avaiable"}
                        <div class="no"> ${data[i].P_no} </div>
                    </div>
                    <div class="${ data[i+1].id ? 'filled': 'empty'} cars">
                        ${data[i+1].id || "Avaiable"} 
                        <div class="no"> ${data[i+1].P_no} </div>
                    </div>
                    <div class="${ data[i+2].id ? 'filled': 'empty'} cars">
                        ${data[i+2].id || "Avaiable"} 
                        <div class="no"> ${data[i+2].P_no} </div>
                    </div>
                    <div class="${ data[i+3].id ? 'filled': 'empty'} cars">
                        ${data[i+3].id || "Avaiable"} 
                        <div class="no"> ${data[i+3].P_no} </div>
                    </div>
                </div>`
            );
        }
    }

    function getReq(fno) {
        $.get({
            url: `/floor${fno}`,
            success: function(data) {
                showMap(JSON.parse(data), fno);
            }
        });
    }


    $("#f1").on("click", function() {
        floorNo = 1;
        openMap(floorNo);
        getReq(floorNo);
    });

    $("#f2").on("click", function() {
       floorNo = 2; 
       openMap(floorNo);
       getReq(floorNo);
    });

    $("#f3").on("click", function() {
       floorNo = 3; 
       openMap(floorNo);
       getReq(floorNo);
    });

    $("#park").on("click", function () {
        const id = $('#input').val();
        const p_no = $('#pno').val();


        //queries pass 
        $.get({
            url: `/update?id=${id}&p_no=${p_no}&floor=${floorNo}`,
            success: function(data) {
                if(data !== "success") {
                    $("#error1").html(data);
                } else {
                    window.location.href = `/index/?floor=${floorNo}`
                    window.reload();
                }
            }
        });
    })

     $("#delete").on("click", function () {
        const id = $('#del').val();
        //queries pass 
        $.get({
            url: `/delete?id=${id}&floor=${floorNo}`,
            success: function(data) {
                console.log(data);
                if(data !== "deleted") {
                    $("#error2").html(data);
                } else {
                    window.location.href = `/index/?floor=${floorNo}`
                    window.reload();
                }
            }
        });
    })

    function openMap(fno) {
        switch(fno) {
            case 1: 
                map1.show();
                map2.hide();
                map3.hide();
                break;

            case 2: 
                map2.show();
                map1.hide();
                map3.hide();
                break;

            case 3:
                map3.show();
                map1.hide();
                map2.hide(); 
                break;
        }
    }

});