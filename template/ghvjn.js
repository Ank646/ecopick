<script>
    const ui=fetch("https://www.postpincode.in/api/getPostalArea.php?pincode=201301")
    xo=xi.json()
    console.log(xo)
    let postoffice=new Array();
    for(i=0;i<xo.length;i++){
postoffice.push(xo[i]["Postoffice"])
    }
  {/* var x = document.getElementById("mySelect");
  var option = document.createElement("option");
  option.text = "Kiwi";
  x.add(option); */}
  console.log(postoffice)
</script>