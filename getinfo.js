// Callback function to handle the server's response of the current set of trees
function displayTrees(response) {
    let treeDiv = document.getElementById("trees");
    let treeData = JSON.parse(response);
    let treeHtml = 
      "<div>" +
        "<div> Tree's class : " + treeData['class'] + "</div" +
        "<div> Tree's number : " + treeData['number'] + "</div" +
        "<div> Tree's value : " + treeData['value'] + "</div" +
      "</div>"

    treeDiv["innerHTML"] = treeHtml;
// these are the method I learnt from https://plotly.com/javascript/, this part set values to x and y axies of scatter plot diagram
    let tempX = treeData['x'].map(v => parseInt(v, 10));
    let tempY = treeData['y'].map(v => parseInt(v, 10));

    var data = [{
      x: tempX,
      y: tempY,
      mode: 'markers',
      type: 'scatter',
      name: 'Tree Data',
      marker: { size: 12 }
    }];

    var layout = {
      title:'Tree Data'
    };

Plotly.newPlot('plot', data, layout);
}

function getTree() {
    let id_element = document.getElementById("tree_id_input");
    let name = id_element.value;
    let query = { "name" : name };
    let queryJSON = JSON.stringify(query);
    console.log("Sending data: "+queryJSON);
    ajaxPostRequest("/getTree", queryJSON, displayTrees);
}
