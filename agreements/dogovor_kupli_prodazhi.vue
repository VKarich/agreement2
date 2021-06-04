<template>
  <div>
    <div class="unselectable" id="unselectable">
      <div id="header">
        <p>
          <strong>ДОГОВОР КУПЛИ-ПРОДАЖИ НЕДВИЖИМОГО ИМУЩЕСТВА № {{ model.number | str_corrector }}</strong>
        </p>
      </div>
      <div id="date">
        <p id="left">
          <strong
            >Город: {{ model.city.firstLetterCaps() | str_corrector }}</strong
          >
        </p>
        <p id="right">
          <strong>Дата: {{ model.date | formatDate | str_corrector }}</strong>
        </p>
      </div>
      <div>
        <div v-if="select_second_step == 'ФЛ'">
          <p>
            {{ model.sellerFullName | str_corrector }},
            {{ model.sellerBirthYear | formatDate | str_corrector }} года рождения, место
            рождения: {{ model.sellerBirthPlace | str_corrector }}, гражданство:
            {{ model.sellerNationality | str_corrector }}, паспорт серия:
            {{ model.sellerPassNumberFirst | str_corrector }} номер:
            {{ model.sellerPassNumberSec | str_corrector }}, выдан:
            {{ model.sellerPassIssuedBy.toUpperCase() | str_corrector }}
            {{ model.sellerPassIssuedOn | formatDate | str_corrector }}, код подразделения:
            {{ model.sellerUnitCode | str_corrector }}, зарегистрированный по
            адресу
            {{ model.sellerRegAddress | str_corrector }}
            {{ model.sellerRepresentDocNum | doverenostFL }}
            {{ model.sellerRepresentDocDate | empty | formatDate | from }}
            {{ model.sellerRepresentDocBy | orgFL }}
            {{ model.sellerRepresentFullName | dovname }}
            {{ model.sellerRepresentPassNumFirst | seriaFL
            }}{{ model.sellerRepresentDocPassNumSec | nomerpas }}
            {{ model.sellerRepresentPassIssuedBy | gaven }}
            {{ model.sellerRepresentPassDate | empty | formatDate }}
            {{ model.sellerRepresentUnitCode | code }}
            {{ model.sellerRepresentRegAddress | addressFL }}
            , именуемый в дальнейшем
            <b>Продавец</b>, с одной стороны, и
          </p>
        </div>
        <div v-else-if="select_second_step == 'ЮЛ'">
          <p>
            <b
              >{{ model.sellerOrgLegalForm | str_corrector }} "{{
                model.sellerOrgName.toUpperCase() | str_corrector
              }}"</b
            >
            в лице {{ model.sellerOrgPossition | str_corrector }}
            {{ model.sellerCeoFullName | str_corrector }}, действующего на
            основании {{ model.sellerOrgDoc.firstLetterCaps() | str_corrector }}
            {{ model.sellerOrgDocNum | nomer }}
            {{ model.sellerOrgDocDate | formatDate | from }}
            {{ model.sellerOrgDocPassNumFirst | seria
            }}{{ model.sellerOrgDocPassNumSec | nomerpas }}
            {{ model.sellerOrgPassIssuedBy | gaven }}
            {{ model.sellerOrgDocPassDate | formatDate }}
            {{ model.sellerOrgUnitCode | code }}
            {{ model.sellerOrgRegAddress | address }} с одной стороны, и
          </p>
        </div>
      </div>
      <div v-if="select_third_step == 'ФЛ'">
        <p>
          {{ model.custFullName | str_corrector }},
          {{ model.custBirthYear | formatDate | str_corrector }} года рождения, место
          рождения: {{ model.custBirthPlace | str_corrector }}, гражданство:
          {{ model.custNationality | str_corrector }}, паспорт серия:
          {{ model.custPassNumberFirst | str_corrector }} номер:
          {{ model.custPassNumberSec | str_corrector }}, выдан:
          {{ model.custPassIssuedBy.toUpperCase() | str_corrector }}
          {{ model.custPassIssuedOn | formatDate | str_corrector }}, код подразделения:
          {{ model.custUnitCode | str_corrector }}, зарегистрированный по адресу
          {{ model.custRegAddress | str_corrector }}
          {{ model.custRepresentDocNum | doverenostFL }}
          {{ model.custRepresentDocDate | empty | formatDate | from }}
          {{ model.custRepresentDocBy | orgFL }}
          {{ model.custRepresentFullName | dovname }}
          {{ model.custRepresentPassNumFirst | seriaFL
          }}{{ model.custRepresentDocPassNumSec | nomerpas }}
          {{ model.custRepresentPassIssuedBy | gaven }}
          {{ model.custRepresentPassDate | empty | formatDate }}
          {{ model.custRepresentUnitCode | code }}
          {{ model.custRepresentRegAddress | addressFL }}
          , именуемый в дальнейшем
          <b>Покупатель</b>, с другой стороны, совместно именуемые
          <b>Стороны, заключили настоящий договор о нижеследующем:</b>
        </p>
      </div>
      <div v-else-if="select_third_step == 'ЮЛ'">
        <p>
          <b
            >{{ model.custOrgLegalForm | str_corrector }} "{{
              model.custOrgName.toUpperCase() | str_corrector
            }}"</b
          >
          в лице {{ model.custOrgPossition | str_corrector }}
          {{ model.custCeoFullName | str_corrector }}, действующего на основании
          {{ model.custOrgDoc.firstLetterCaps() | str_corrector }}
          {{ model.custOrgDocNum | nomer }}
          {{ model.custOrgDocDate | formatDate | from }}
          {{ model.custOrgDocPassNumFirst | seria
          }}{{ model.custOrgDocPassNumSec | nomerpas }}
          {{ model.custOrgPassIssuedBy | gaven }}
          {{ model.custOrgDocPassDate | formatDate }}
          {{ model.custOrgUnitCode | code }}
          {{ model.custOrgRegAddress | address }}
          , именуемый в дальнейшем
          <b>Покупатель</b>, с другой стороны, совместно именуемые
          <b>Стороны, заключили настоящий договор о нижеследующем:</b>
        </p>
      </div>
      <div>
        <p>
          <b>1. Продавец</b> продал, а <b>Покупатель</b> приобрел в
          собственность следующий(-щие) <b>Объект(ы)</b> недвижимого имущества:
        </p>
      </div>
      <div>
        <p v-if="model.propertyName == 'Квартира'">
          {{ model.propertyName | str_corrector }}, общей площадью
          {{ model.propertyFloorArea | str_corrector }} кв.м, количество комнат:
          {{ model.propertyNumRoom | str_corrector }}, этаж:
          {{ model.propertyLevel | str_corrector }}, расположенная по адресу:
          {{ model.propertyAddress | str_corrector }}, кадастровый номер:
          {{ model.propertyUniqueIdentifier | str_corrector }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ model.propertyDoc | str_corrector }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ model.regDocDate | formatDate | str_corrector }} №{{
            model.regDocNumber | str_corrector
          }}.
        </p>
        <p v-else-if="model.propertyName == 'Земельный участок'">
          {{ model.propertyName | str_corrector }}, общей площадью
          {{ model.propertyFloorArea | str_corrector }} кв.м, категория земель:
          {{ model.propertyLandCat | str_corrector }}, разрешенное
          использование: {{ model.propertyLandUsed | str_corrector }},
          расположенный по адресу: {{ model.propertyAddress | str_corrector }},
          кадастровый номер:
          {{ model.propertyUniqueIdentifier | str_corrector }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ model.propertyDoc | str_corrector }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ model.regDocDate | formatDate | str_corrector }} №{{
            model.regDocNumber | str_corrector
          }}.
        </p>
        <p v-else-if="model.propertyName == 'Жилой дом'">
          {{ model.propertyName | str_corrector }}, общей площадью
          {{ model.propertyFloorArea | str_corrector }} кв.м, количество комнат:
          {{ model.propertyNumRoom | str_corrector }}, этажей:
          {{ model.propertyLevel | str_corrector }}, расположенный по адресу:
          {{ model.propertyAddress | str_corrector }}, кадастровый номер:
          {{ model.propertyUniqueIdentifier | str_corrector }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ model.propertyDoc | str_corrector }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ model.regDocDate | formatDate | str_corrector }} №{{
            model.regDocNumber | str_corrector
          }}.
        </p>
      </div>
      




      <div v-if="add">
        <p v-if="model.propertyName15 == 'Квартира'">
          {{ model.propertyName15 | str_corrector }}, общей площадью
          {{ model.propertyFloorArea15 | str_corrector }} кв.м, количество комнат:
          {{ model.propertyNumRoom15 | str_corrector }}, этаж:
          {{ model.propertyLevel15 | str_corrector }}, расположенная по адресу:
          {{ model.propertyAddress15 | str_corrector }}, кадастровый номер:
          {{ model.propertyUniqueIdentifier15 | str_corrector }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ model.propertyDoc15 | str_corrector }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ model.regDocDate15 | formatDate | str_corrector }} №{{
            model.regDocNumber15 | str_corrector
          }}.
        </p>
        <p v-else-if="model.propertyName15 == 'Земельный участок'">
          {{ model.propertyName15 | str_corrector }}, общей площадью
          {{ model.propertyFloorArea15 | str_corrector }} кв.м, категория земель:
          {{ model.propertyLandCat15 | str_corrector }}, разрешенное
          использование: {{ model.propertyLandUsed15 | str_corrector }},
          расположенный по адресу: {{ model.propertyAddress15 | str_corrector }},
          кадастровый номер:
          {{ model.propertyUniqueIdentifier15 | str_corrector }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ model.propertyDoc15 | str_corrector }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ model.regDocDate15 | formatDate | str_corrector }} №{{
            model.regDocNumber15 | str_corrector
          }}.
        </p>
        <p v-else-if="model.propertyName15 == 'Жилой дом'">
          {{ model.propertyName15 | str_corrector }}, общей площадью
          {{ model.propertyFloorArea15 | str_corrector }} кв.м, количество комнат:
          {{ model.propertyNumRoom15 | str_corrector }}, этажей:
          {{ model.propertyLevel15 | str_corrector }}, расположенный по адресу:
          {{ model.propertyAddress15 | str_corrector }}, кадастровый номер:
          {{ model.propertyUniqueIdentifier15 | str_corrector }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ model.propertyDoc15 | str_corrector }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ model.regDocDate15 | formatDate | str_corrector }} №{{
            model.regDocNumber15 | str_corrector
          }}.
        </p>
      </div>







      <div>
        <p>
          <b>2.</b> Стоимость недвижимого имущества составляет
          <b
            >{{ model.cost | numeral("₽0,0.00") }} ({{
              model.cost | rubles | str_corrector
            }})</b
          >. Цена является окончательной и изменению не подлежит. Расчет между
          сторонами осуществляется в следующем порядке:
        </p>
      </div>
      <div v-if="JSON.stringify(model.payMethod).match('Материнский капитал')">
        <p>
          Оплата суммы в размере
          <b
            >{{ model.paySumMatCap | numeral("₽0,0.00") }} ({{
              model.paySumMatCap | rubles | str_corrector
            }})</b
          >
          осуществляется <b>Покупателем</b> за счет средств
          <b>государственного сертификата на материнский (семейный) капитал</b>,
          выданного на основании решения
          <b>{{ model.matcap.toUpperCase() | str_corrector }}</b> от
          {{ model.matcapDesDate | formatDate | str_corrector }} №
          {{ model.matcapDesNum | str_corrector }}, серии
          {{ model.matcapSer | str_corrector }} №
          {{ model.matcapNum | str_corrector }}, выданного
          {{ model.matcapDate | formatDate | str_corrector }} на имя
          <b>{{ model.matcapOwner | str_corrector }}</b
          >, в соответствии с Федеральным законом
          <b
            >«О дополнительных мерах государственной поддержки семей, имеющих
            детей»</b
          >, после государственной регистрации перехода права собственности на
          имя <b>Покупателя</b>, в установленный законом срок.
        </p>
      </div>
      <div v-if="JSON.stringify(model.payMethod).match('Рассрочка')">
        <p>
          Денежные средства в размере
          <b
            >{{ model.paySumRS | numeral("₽0,0.00") }} ({{
              model.paySumRS | rubles | str_corrector
            }})</b
          >
          <b> Покупатель</b> обязуется оплатить <b>Продавцу</b> согласно
          следующему графику:
        </p>
        <br />
        <div id="header">
          <strong>График платежей:</strong>
        </div>
        <table>
          <tr>
            <td>№ п/п</td>
            <td>Дата платежа (с / по включительно)</td>
            <td>Размер платежа (в рублях)</td>
          </tr>
          <tr v-for="one in Number(model.quantityPayments)" :key="one">
            <td>{{ one }}</td>
            <td>
              <p v-for="(item, index) in model.rsPaymentDate[one]" :key="index">
                {{ item | formatDate }}
              </p>
            </td>
            <td>
              <b>{{ model.rsPayment[one] | numeral("₽0,0.00") }}</b>
            </td>
          </tr>
        </table>
        <div v-if="JSON.stringify(model.payMethod).match('Рассрочка')">
          <span
            >Оплата по договору осуществляется в срок до
            {{ model.zlgPayTermDate | formatDate | str_corrector }}</span
          >
        </div>
        <div v-if="JSON.stringify(model.payMethod).match('Рассрочка')">
          <p v-if="model.zlgPay == 'Имеется'">
            Стороны договорились о том, что до полного расчета по основному
            договору купли-продажи право залога на отчуждаемую квартиру в силу
            закона (в соответствии с ч. 5 ст. 488 Гражданского кодекса РФ)
            устанавливается в пользу «Продавца».
          </p>
          <p v-else-if="model.zlgPay == 'Не имеется'">
            Стороны договорились о том, что до полного расчета по основному
            договору купли-продажи право залога на отчуждаемую квартиру в силу
            закона (в соответствии с ч. 5 ст. 488 Гражданского кодекса РФ) в
            пользу «Продавца» не возникает.
          </p>
        </div>
      </div>

      <div v-if="JSON.stringify(model.payMethod).match('Ипотека физ. лица')">
        <p>
          Денежные средства в размере
          <b
            >{{ model.paySumFL | numeral("₽0,0.00") }} ({{
              model.paySumFL | rubles | str_corrector
            }})</b
          >
          <b> Покупатель</b> обязуется оплатить <b>Продавцу</b> согласно
          следующему графику:
        </p>
        <br />
        <div id="header">
          <strong>График платежей:</strong>
        </div>
        <table>
          <tr>
            <td>№ п/п</td>
            <td>Дата платежа (с / по включительно)</td>
            <td>Размер платежа (в рублях)</td>
          </tr>
          <tr v-for="one in Number(model.quantityPaymentsFL)" :key="one">
            <td>{{ one }}</td>
            <td>
              <p
                v-for="(item, index) in model.rsPaymentDateFL[one]"
                :key="index"
              >
                {{ item | formatDate }}
              </p>
            </td>
            <td>
              <b>{{ model.rsPaymentFL[one] | numeral("₽0,0.00") }}</b>
            </td>
          </tr>
        </table>
        <div v-if="JSON.stringify(model.payMethod).match('Ипотека физ. лица')">
          <span
            >Оплата по договору осуществляется в срок до
            {{ model.zlgPayTermDate | formatDate | str_corrector }}</span
          >
        </div>
        <div v-if="JSON.stringify(model.payMethod).match('Ипотека физ. лица')">
          <p>
            Стороны договорились о том, что до полного расчета по основному
            договору купли-продажи право залога на отчуждаемую квартиру в силу
            закона (в соответствии с ч. 5 ст. 488 Гражданского кодекса РФ)
            устанавливается в пользу «Продавца».
          </p>
        </div>
      </div>

      <div v-if="JSON.stringify(model.payMethod).match('Наличный расчет')">
        <p>
          Оплата стоимости имущества в размере
          <b
            >{{ model.nal | numeral("₽0,0.00") }} ({{
              model.nal | rubles | str_corrector
            }})</b
          >
          осуществляется <b> Покупателем</b> за счет собственных наличных
          денежных средств.
        </p>
      </div>

      <div v-if="JSON.stringify(model.payMethod).match('Безналичный расчет')">
        <p>
          Оплата стоимости имущества в размере
          <b
            >{{ model.bznal | numeral("₽0,0.00") }} ({{
              model.bznal | rubles | str_corrector
            }})</b
          >
          осуществляется <b> Покупателем</b> за счет собственных наличных
          денежных средств путем перечисления указанной суммы на счет
          <b>Продавца</b> № {{ model.bznalBankNum }}, открытый в
          {{ model.bznalBankName }}.
        </p>
      </div>

      <div v-if="JSON.stringify(model.payMethod).match('Ипотека банка')">
        <p>
          Оплата суммы в размере
          <b
            >{{ model.paySumIB | numeral("₽0,0.00") }} ({{
              model.paySumIB | rubles | str_corrector
            }})</b
          >
          осуществляется <b>Покупателем</b> за счет кредитных средств
          предоставленных
          <b>Покупателю {{ model.crBankName.toUpperCase() | str_corrector }}</b>
          (далее - Банк), в соответствии с кредитным договором №
          {{ model.crBankNumber | str_corrector }} от
          <b>{{ model.crBankDocDate | formatDate | str_corrector }}</b
          >, заключенным в городе
          {{ model.crBankDocTown | str_corrector }} между Банком и
          <b>Покупателем</b> (далее – Кредитный договор) сроком на
          <b>{{ model.crBankDocQMonth | str_corrector }}</b>
          {{ model.crBankDocQMonth | months }} под процентную ставку Банка.
          <br />
          <br />
          В соответствии со ст.77 ФЗ «Об ипотеке (залоге недвижимости)», с
          момента государственной регистрации перехода права собственности на
          квартиру к Покупателю, квартира считается находящейся в залоге у
          Банка.
          <br />
          <br />
          Последующая ипотека квартиры может быть осуществлена только с
          письменного согласия Банка.
          <br />
          <br />
          Залогодержателем является
          <b
            >{{ model.crBankName.toUpperCase() | str_corrector }} (РЕКВИЗИТЫ
            БАНКА: ОГРН: {{ model.crBankOgrn | str_corrector }}, ИНН:
            {{ model.crBankInn | str_corrector }}, КПП:
            {{ model.crBankKpp | str_corrector }}, Р/С:
            {{ model.crBankRs | str_corrector }}, К/С:
            {{ model.crBankKs | str_corrector }}, БИК:
            {{ model.crBankBik | str_corrector }}, Местонахождение банка:
            {{ model.crBankAddress | str_corrector }}, Почтовый адрес банка:
            {{ model.crBankPostAddress | str_corrector }})</b
          >
          Залогодателем – Покупатель.
          <br />
          <br />
          Права Залогодержателя удостоверяются закладной.
        </p>
      </div>
      <div v-if="JSON.stringify(model.payMethod).match('Аккредитив')">
        <p>
          Оплата суммы в размере
          <b
            >{{ model.paySumA | numeral("₽0,0.00") }} ({{
              model.paySumA | rubles | str_corrector
            }})</b
          >
          осуществляется <b>Покупателем</b> путем открытия документарного
          безотзывного покрытого аккредитива на сумму
          <b
            >{{ model.paySumA | numeral("₽0,0.00") }} ({{
              model.paySumA | rubles | str_corrector
            }})</b
          >
          в пользу <b>Продавца </b> в день подписания настоящего договора,
          сроком действия {{ model.acrDays | str_corrector }}
          {{ model.acrDays | days | str_corrector }} со дня подписания
          настоящего договора (далее – «Аккредитив»). Покрытие аккредитива
          осуществляется <b>Покупателем</b> за счет собственных средств.
        </p>
        <br />
        <p>
          Банком – эмитентом и исполняющим банком по аккредитиву является
          {{ model.acrBankName.toUpperCase() | str_corrector }} (далее – «Банк»)
          в г. {{ model.acrBankTown.firstLetterCaps() | str_corrector }}
        </p>
        <br />
        <p>
          Раскрытие аккредитива осуществляется Банком в течение 3-х рабочих дней
          с момента предоставления <b>Продавцом</b> до истечения срока действия
          аккредитива документа, подтверждающего переход права собственности на
          квартиру.
        </p>
        <br />
        <p>
          В случае намерения <b>Покупателя</b> изменить условия аккредитива, он
          представляет в Банк соответствующее распоряжение.
        </p>
        <br />
        <p>
          Банк уведомляет <b>Продавца</b> и запрашивает его согласие (акцепт) на
          изменение условий аккредитива. По получении согласия
          <b>Продавца</b> Банк исполняет распоряжение <b>Покупателя</b> на
          внесение изменений в условия аккредитива. При этом внесение изменений
          в настоящий договор не требуется.
        </p>
        <br />
        <p>
          Счетом получателя денежных средств по аккредитиву является счет
          <b>Продавца</b> № {{ model.acrBankSellerNumber | str_corrector }},
          открытый в
          {{ model.acrBankSellerName.toUpperCase() | str_corrector }} (далее –
          «Счет «Продавца»).
        </p>
        <br />
        <p>
          Затраты Банка, связанные с открытием и исполнением аккредитива,
          относятся на счет <b>Покупателя</b> в соответствии с тарифами Банка.
        </p>
        <br />
        <p>
          Если <b>Продавец</b> не сможет получить денежные средства с
          аккредитива, открытого в соответствии с условиями настоящего договора,
          по причинам, вызванным действиями <b>Покупателя</b>, а также в случае,
          если аккредитив окажется закрытым к моменту фактического получения
          настоящего договора с отместкой о государственной регистрации перехода
          права собственности на квартиру от <b>Продавца</b> к
          <b>Покупателю</b> по причине приостановки или задержки последней, в
          связи с истечением срока действия аккредитива, <b>Покупатель</b> будет
          обязан либо продлить срок действия аккредитива, либо оплатить цену
          настоящего договора, путем перечисления денежных средств на расчетный
          счет <b>Продавца</b>, указанный последним, либо иным способом, не
          запрещенным действующим законодательством Российской Федерации, по
          согласованию с <b>Продавцом</b>, в течение 5 (пяти) рабочих дней со
          дня государственной регистрации перехода права собственности на
          квартиру от <b>Продавца</b> к <b>Покупателю</b>. В противном случае
          <b>Покупатель</b> будет считаться нарушившим срок оплаты.
        </p>
        <br />
        <p>
          В случае одностороннего отказа <b>Покупателя</b> от исполнения
          настоящего договора до государственной регистрации перехода права
          собственности на квартиру от <b>Продавца</b> к <b>Покупателю</b>,
          денежные средства с аккредитива возвращаются <b>Покупателю</b>, при
          этом затраты Банка, связанные с открытием и проведением расчетов по
          аккредитиву, относятся на счет <b>Покупателя</b> в соответствии с
          тарифами Банка и удерживаются Банком при возврате суммы аккредитива.
        </p>
      </div>
      <div>
        <p>
          <b>3. Продавец</b> гарантирует, что до заключения настоящего договора,
          отчуждаемое недвижимое имущество никому другому не продано, не
          подарено, не обещано в дар, не заложено, в споре и под арестом
          (запрещением) не состоит, каких-либо обременений не имеется.
        </p>
        <p v-if="model.propertyName == 'Квартира'">
          <b>Продавец</b> гарантирует и подтвердил <b>Покупателю</b> отсутствие
          задолженности по коммунальным платежам за Квартиру, она пригодна для
          проживания, зарегистрированные или имеющие право пожизненного
          проживания лица отсутствуют.
        </p>
      </div>
      <div>
        <p>
          Кроме того, <b>Продавец</b> гарантирует <b>Покупателю</b>, что в
          отношении <b>Продавца</b> не производятся действия и отсутствуют
          обязательства о несостоятельности (банкротстве). <b>Покупатель</b> до
          заключения настоящего договора осмотрел приобретаемое недвижимое
          имущество, ему известна его техническая характеристика и правовой
          режим. <b>Продавец</b> гарантирует, что недвижимое имущество не имеет
          никаких скрытых недостатков, которые невозможно устранить инженерным
          путем.
        </p>
      </div>
      <div>
        <p>
          <b>4.</b>
          <span
            >Стороны договора подтверждают, что не лишены дееспособности, не
            состоят под опекой и попечительством, не страдают заболеваниями,
            препятствующими осознать суть договора, а также отсутствуют
            обстоятельства, вынуждающие совершить настоящий договор на крайне
            невыгодных для них условиях. Кроме того, Продавец гарантирует
            Покупателю, что в отношении Продавца не производятся действия и
            отсутствуют обязательства о несостоятельности (банкротстве) Продавца
            и (или) Продавец не признан банкротом. Подписание сторонами
            настоящего договора подтверждает отсутствие у Покупателя каких-либо
            данных о неплатежеспособности Продавца.
          </span>
        </p>
      </div>
      <div>
        <p>Также <b>Продавец</b> подтверждает и гарантирует, что:</p>
      </div>
      <div>
        <p>
          - не имеет долгов и/или любых иных неисполненных обязательств, которые
          могут повлечь его банкротство как физического лица в течение
          ближайшего месяца, что ему ничего не известно о кредиторах, которые
          могут обратиться в суд с иском о признании банкротом физического лица,
          и что он сам не планирует обращаться в суд о признании себя банкротом.
          - не является ответчиком в суде как физическое лицо, в отношении него
          не ведется исполнительное производство, а равно уголовное
          преследование, с возможным предъявлением гражданского иска, вследствие
          чего, на недвижимость может быть наложен арест, и/или обращено
          взыскание, или конфискация в пользу третьих лиц. Недвижимость не
          входит в состав уставного капитала юридического лица, в отношении
          которого начата процедура банкротства, реорганизации или ликвидации.
        </p>
      </div>
      <div>
        <p>
          <b>5.</b>
          <span
            >Стороны настоящего договора несут ответственность за совершение
            любых действий, противоречащих действующему законодательству
            Российской Федерации.</span
          >
        </p>
      </div>
      <div>
        <p>
          <b>6.</b> Переход права собственности на отчуждаемое недвижимое
          имущество от <b>Продавца</b> к <b>Покупателю</b> подлежит
          государственной регистрации в Управлении Федеральной службы
          государственной регистрации, кадастра и картографии по области
          регистрации объекта.
        </p>
      </div>
      <div>
        <p>
          <b>7.</b>
          <span
            >Передача отчуждаемого недвижимого имущества
            <b>Продавцом Покупателю</b> осуществляется путем подписания
            настоящего договора, который имеет силу Акта приема-передачи
            недвижимого имущества.</span
          >
        </p>
      </div>
      <div>
        <p>
          <b>8.</b>
          <span
            >Настоящий договор содержит весь объем соглашений между сторонами в
            отношении предмета настоящего договора, отменяет и делает
            недействительными все другие обязательства или представления,
            которые могли быть приняты или сделаны сторонами, будь то в устной
            или письменной форме, до заключения настоящего договора.</span
          >
        </p>
      </div>
      <div>
        <p>
          <b>9.</b>
          <span
            >Настоящий договор составлен в 3-х экземплярах, один из которых
            остается в делах Управления Федеральной службы государственной
            регистрации, кадастра и картографии по области регистрации объекта,
            один выдается <b>Продавцу</b> и один выдается
            <b>Покупателю</b>.</span
          >
        </p>
      </div>
      <div>
        <p>
          <b>10.</b>
          <span
            >Настоящий договор сторонами прочитан, претензий и замечаний стороны
            не имеют. Последствия совершения настоящей сделки сторонам известны.
            Стороны заключают настоящий договор добровольно, не вследствие
            стечения тяжелых обстоятельств или на крайне невыгодных для себя
            условиях, настоящий договор не является для Сторон кабальной
            сделкой. Стороны подтверждают, что они в дееспособности не
            ограничены; под опекой, попечительством, а также патронажем не
            состоят; по состоянию здоровья могут самостоятельно осуществлять и
            защищать свои права и исполнять обязанности; не страдают
            заболеваниями, препятствующими осознавать суть подписываемого
            договора и обстоятельств его заключения.</span
          >
        </p>
      </div>
      <div>
        <p>
          <b>11.</b>
          <span
            >Расходы, связанные с заключением настоящего договора и
            государственной регистрацией перехода права собственности на
            недвижимое имущество, несет <b>Покупатель</b>.</span
          >
        </p>
      </div>
      <div id="signature">
        <p id="header">
          <strong>ПОДПИСИ СТОРОН:</strong>
        </p>
        <div class="lf" v-if="select_second_step == 'ФЛ'">
          <p>
            <b>Продавец:</b>
          </p>
          <p>
            {{ model.sellerFullName | str_corrector }}
          </p>
        </div>
        <div class="rf" v-if="select_third_step == 'ФЛ'">
          <p>
            <b>Покупатель:</b>
          </p>
          <p>
            {{ model.custFullName | str_corrector }}
          </p>
        </div>
        <div class="lf" v-if="select_second_step == 'ЮЛ'">
          <p>
            <b>Продавец:</b>
          </p>
          <p>
            {{ model.sellerOrgLegalForm | str_corrector }} "{{
              model.sellerOrgName | str_corrector
            }}"
          </p>
          <p>
            Юридический адрес: {{ model.sellerOrgRegAddressUR | str_corrector }}
          </p>
          <p>ОГРН: {{ model.sellerOrgOGRN | str_corrector }}</p>
          <p>ИНН: {{ model.sellerOrgINN | str_corrector }}</p>
          <p>КПП: {{ model.sellerOrgKPP | str_corrector }}</p>
          <p>Р/С: {{ model.sellerOrgRS | str_corrector }}</p>
          <p>КС: {{ model.sellerOrgKS | str_corrector }}</p>
          <p>Банк: {{ model.sellerOrgBank | str_corrector }}</p>
          <p>БИК: {{ model.sellerOrgBankBik | str_corrector }}</p>
          <p>Номер телефона: {{ model.sellerOrgTel | str_corrector }}</p>
          <p>
            Почтовый адрес: {{ model.sellerOrgPostAddress | str_corrector }}
          </p>
          <p>В лице: {{ model.sellerCeoFullName | str_corrector }}</p>
        </div>
        <div class="rf" v-if="select_third_step == 'ЮЛ'">
          <p>
            <b>Покупатель:</b>
          </p>
          <p>
            {{ model.custOrgLegalForm | str_corrector }} "{{
              model.custOrgName | str_corrector
            }}"
          </p>
          <p>
            Юридический адрес: {{ model.custOrgRegAddressUR | str_corrector }}
          </p>
          <p>ОГРН: {{ model.custOrgOGRN | str_corrector }}</p>
          <p>ИНН: {{ model.custOrgINN | str_corrector }}</p>
          <p>КПП: {{ model.custOrgKPP | str_corrector }}</p>
          <p>Р/С: {{ model.custOrgRS | str_corrector }}</p>
          <p>КС: {{ model.custOrgKS | str_corrector }}</p>
          <p>Банк: {{ model.custOrgBank | str_corrector }}</p>
          <p>БИК: {{ model.custOrgBankBik | str_corrector }}</p>
          <p>Номер телефона: {{ model.custOrgTel | str_corrector }}</p>
          <p>Почтовый адрес: {{ model.custOrgPostAddress | str_corrector }}</p>
          <p>В лице: {{ model.custFullName | str_corrector }}</p>
        </div>
      </div>

      <div class="receipt" v-if="JSON.stringify(model.payMethod).match('Наличный расчет')">
        <div id="header">
        <p>
          <strong>Расписка о получении денежных средств в счет оплаты 
по договору купли-продажи № {{ model.number | str_corrector }} от {{ model.date | formatDate | str_corrector }} г.
</strong>
        </p>
      </div>
      <div id="date">
        <p id="left">
          <strong
            >Город: {{ model.city.firstLetterCaps() | str_corrector }}</strong
          >
        </p>
        <p id="right">
          <strong>Дата: {{ model.date | formatDate | str_corrector }}</strong>
        </p>
      </div>
      <p>
         Гр. {{ model.sellerFullName | str_corrector }}, именуемый в дальнейшем <b>«Продавец»</b> и
      </p>
      <p>
        Гр. {{ model.custFullName | str_corrector }}, именуемый в дальнейшем <b>«Покупатель»</b>, с другой стороны, совместно именуемые <b>«Стороны»</b>,
      </p>
      <br>
      <p>
        составили настоящую расписку о нижеследующем:
      </p>
      <br>
      <p>
        <b>1. «Покупатель»</b> передал, а <b>«Продавец»</b> принял денежные средства в размере <b
            >{{ model.nal | numeral("₽0,0.00") }} ({{
              model.nal | rubles | str_corrector
            }})</b
          > в счет оплаты недвижимого имущества ({{ model.propertyName | str_corrector }}, общей площадью
          {{ model.propertyFloorArea | str_corrector }} кв.м) по Договору купли-продажи № {{ model.number | str_corrector }} от {{ model.date | formatDate | str_corrector }} г., заключенному между <b>«Продавцом»</b> и <b>«Покупателем»</b>.
      </p>
      <br>
      <p>
      <b>2. «Стороны»</b> подтверждают, что оплата по Договору произведена в полном объеме. Претензии по оплате у Сторон отсутствуют.
      </p>
      <br>
      <p v-if="JSON.stringify(model.avance).match('Имеется')">
        <b>3. «Продавец»</b> подтверждает, что авансовый платеж в размере <b
            >{{ model.avancesum | numeral("₽0,0.00") }} ({{
              model.avancesum | rubles | str_corrector
            }})</b
          > был передан <b>«Покупателем» «Продавцу»</b>  до подписания Договора купли-продажи недвижимого имущества № {{ model.number | str_corrector }} от {{ model.date | formatDate | str_corrector }} г.
      </p>
      <br>
      <div class="lf" v-if="select_second_step == 'ФЛ'">
          <p>
            <b>Продавец:</b>
          </p>
          <p>
            _______________________
          </p>
          <p>
            Гр. {{ model.sellerFullName | str_corrector }}
          </p>
        </div>
        <div class="rf" v-if="select_third_step == 'ФЛ'">
          <p>
            <b>Покупатель:</b>
          </p>
          <p>
            _______________________
          </p>
          <p>
            Гр. {{ model.custFullName | str_corrector }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="module">
/* eslint-disable */ 
import Vue from "vue";
import html2canvas from "html2canvas";
import jsPDF from "jspdf";
import moment from 'moment'

String.prototype.firstLetterCaps = function () {
  return this.charAt(0).toUpperCase() + this.slice(1);
};

var rubles = require('rubles').rubles;

Vue.filter('rubles', function (value) {
  if (!value) return '';
  return rubles(value);
})

Vue.filter('months', function (value) {
  if ((value.toString().substr(-1) == 1) && (value !== 11) && (value !== 12) && (value !== 13) && (value !== 14) && (value !== 111) && (value !== 913)) return 'месяц';
  if (((value.toString().substr(-1) == 2) || (value.toString().substr(-1) == 3) || (value.toString().substr(-1) == 4)) && ((value !== 11) && (value !== 12) && (value !== 13) && (value !== 14) && (value !== 111) && (value !== 913))) return 'месяца';
  return 'месяцев'
})

Vue.filter('days', function (value) {
  if ((value.toString().substr(-1) == 1) && (value !== 11) && (value !== 12) && (value !== 13) && (value !== 14) && (value !== 111) && (value !== 913)) return 'день';
  if (((value.toString().substr(-1) == 2) || (value.toString().substr(-1) == 3) || (value.toString().substr(-1) == 4)) && ((value !== 11) && (value !== 12) && (value !== 13) && (value !== 14) && (value !== 111) && (value !== 913))) return 'дня';
  return 'дней'
})

Vue.filter('str_corrector', function (value) {
  if (!value) return '_________________';
  return (value)
})

Vue.filter('empty', function (value) {
  if (value == null) {
    return ''
  }
  return (value)
});

Vue.filter('formatDate', function (value) {
  if (value) {
    return (moment(String(value)).format('DD.MM.YYYY'))
  }
  return ''
});

Vue.filter("dovname", function (value) {
  if (value) return " на имя " + value + ". Данные доверенности:";
});

Vue.filter("orgFL", function (value) {
  if (value) return ", выданной  " + value;
  return "";
});

Vue.filter("seria", function (value) {
  if (value) return ", (Паспортные данные: серия: " + value + ",";
});

Vue.filter("seriaFL", function (value) {
  if (value) return " Паспортные данные: серия: " + value + ",";
});

Vue.filter("nomerpas", function (value) {
  if (value) return " номер: " + value + ",";
});

Vue.filter("doverenostFL", function (value) {
  if (value)
    return ", в лице представителя на основании доверенности № " + value;
  return "";
});

Vue.filter("gaven", function (value) {
  if (value) return "выдан: " + value + ",";
});

Vue.filter("code", function (value) {
  if (value) return "код подразделения: " + value + ",";
});

Vue.filter("address", function (value) {
  if (value) return "адрес регистрации: " + value + "),";
});

Vue.filter("addressFL", function (value) {
  if (value) return "адрес регистрации: " + value;
});

Vue.filter("nomer", function (value) {
  if (value) return "№" + value;
  return "";
});

Vue.filter("from", function (value) {
  if (value) return "от" + " " + value;
  return "";
});

Vue.filter("payMeth", function (value) {
  if (value == "Материнский капитал") {
    return (value = "Материнского капитала");
  }
  if (value == "Рассрочка") {
    return (value = "Рассрочки");
  }
  if (value == "Ипотека банка") {
    return (value = "Ипотеки банка");
  }
  if (value == "Ипотека физ. лица") {
    return (value = "Ипотеки физического лица");
  }
  if (value == "Аккредитив") {
    return (value = "Аккредитива");
  }
  if (value == "Залог в пользу продавца") {
    return (value = "Залога в пользу продавца");
  }
  return value;
});

export default {
  name: "dogovor_kupli_prodazhi",
  props: {
    model: Object,
    schema: Object,
    select_second_step: String,
    select_third_step: String,
    plain: Function,
    add: Boolean
  },
  methods: {
    printpdf() {
      const filename = "ThisIsYourPDFFilename.pdf";

      html2canvas(document.querySelector("#unselectable")).then((canvas) => {
        let pdf = new jsPDF("p", "mm", "a4");
        pdf.addImage(canvas.toDataURL("image/png"), "PNG", 0, 0, 211, 298);
        pdf.save(filename);
      });
    },
    Export2Doc(element, filename = "") {
      let preHtml =
        "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>Export HTML To Doc</title></head><body>";
      let postHtml = "</body></html>";
      let html =
        preHtml + document.getElementById(element).innerHTML + postHtml;

      let blob = new Blob(["\ufeff", html], {
        type: "application/msword",
      });

      // Specify link url
      let url =
        "data:application/vnd.ms-word;charset=utf-8," +
        encodeURIComponent(html);

      // Specify file name
      filename = filename ? filename + ".docx" : "document.docx";

      // Create download link element
      let downloadLink = document.createElement("a");

      document.body.appendChild(downloadLink);

      if (navigator.msSaveOrOpenBlob) {
        navigator.msSaveOrOpenBlob(blob, filename);
      } else {
        // Create a link to the file
        downloadLink.href = url;

        // Setting the file name
        downloadLink.download = filename;

        //triggering the function
        downloadLink.click();
      }

      document.body.removeChild(downloadLink);
    },
  },
};
</script>

<style scoped>
div,
table {
  margin-bottom: 20px;
}
h1 {
  text-align: center;
}
#header {
  text-align: center;
  margin-bottom: 20px;
}
strong {
  text-align: center;
}
#signature {
  display: table;
  width: 100%;
}
.lf {
  display: table-cell;
  float: left;
  max-width: 50%;
}
.rf {
  display: table-cell;
  float: right;
  max-width: 50%;
}
#main {
  display: block;
}
.unselectable {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Chrome/Safari/Opera */
  -khtml-user-select: none; /* Konqueror */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently*/
  opacity: 0.8;
}
.watermark {
  opacity: 0.5;
  color: rgb(236, 29, 29);
  position: absolute;
  top: auto;
  left: 80%;
}
.flou {
  color: transparent;
  text-shadow: 0 0 8px #999;
  font-weight: normal;
  filter: blur(5px);
  -webkit-filter: blur(5px);
}
table {
  border: black solid 1px;
  width: 100%;
  table-layout: auto;
  text-align: center;
}
tr td {
  border: black solid 1px;
  padding: 10px;
  text-align: center;
}
.receipt {
  padding-top: 60px;
}
</style>
