
/**
function d(s) {
    get2(s);


}

function get2(fileName) {
    if (!(fileName == "")) {
        var link = document.getElementById("link2");
        link.href = "../cmdZIP/" + fileName + ".zip";
        link.click();



    } else {
        var list = document.getElementById("list").value;
        console.log(list);
    }

}
*/
const sample = document.getElementById("sample");
const text = document.getElementById("text")

//ダイアログでファイルが選択された時
sample.addEventListener("change", function (event) {

  const file = event.target.files;

  //FileReaderの作成
  const reader = new FileReader();
  //テキスト形式で読み込む
  reader.readAsText(file[0]);

  //読込終了後の処理
  reader.onload = function () {
    //テキストエリアに表示する
    text.value = reader.result;
  }
});