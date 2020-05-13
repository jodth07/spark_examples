package com.dimanche.examples

import spray.json._
import DefaultJsonProtocol._

//val json: JsValue = Json.parse("""{"a":1}""")
object Runner {

  def main(args: Array[String]): Unit = {
//    println("Hello World")

    val data = """{
                 |  "id": "file",
                 |  "value": "File",
                 |  "popup": {
                 |    "menuitem": [
                 |      {"value": "New", "onclick": "CreateNewDoc()"},
                 |      {"value": "Open", "onclick": "OpenDoc()"},
                 |      {"value": "Close", "onclick": "CloseDoc()"}
                 |    ]
                 |  }
                 |}""".stripMargin

//    println(data)
//    val data1 = {"menu":{"id":"file","popup":{"menuitem":[{"onclick":"CreateNewDoc()","value":"New"},{"onclick":"OpenDoc()","value":"Open"},{"onclick":"CloseDoc()","value":"Close"}]},"value":"File"}}
//    val data2 =  "{"menu":{"id":"file","popup":{"menuitem":[{"onclick":"CreateNewDoc()","value":"New"},{"onclick":"OpenDoc()","value":"Open"},{"onclick":"CloseDoc()","value":"Close"}]},"value":"File"}}"
//    val data3 =  """{"menu":{"id":"file","popup":{"menuitem":[{"onclick":"CreateNewDoc()","value":"New"},{"onclick":"OpenDoc()","value":"Open"},{"onclick":"CloseDoc()","value":"Close"}]},"value":"File"}}"""



    val parsed = data.parseJson
    println(parsed)


  }

}
