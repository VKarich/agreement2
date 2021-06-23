<template>
  <div>
    <div class="unselectable" id="unselectable">
      <div id="header">
        <p>
          <strong
            >ДОГОВОР КУПЛИ-ПРОДАЖИ НЕДВИЖИМОГО ИМУЩЕСТВА №
            {{ data_model.number }}</strong
          >
        </p>
      </div>
      <div id="date">
        <p id="left">
          <strong
            >Город: {{ data_model.city.firstLetterCaps() }}</strong
          >
        </p>
        <p id="right">
          <strong>Дата: {{ data_model.date }}</strong>
        </p>
      </div>
      <div>
        <div v-if="select_second_step == 'ФЛ'">
          <p>
            {{ data_model.sellerFullName }},
            {{ data_model.sellerBirthYear }} года
            рождения, место рождения:
            {{ data_model.sellerBirthPlace }}, гражданство:
            {{ data_model.sellerNationality }}, паспорт серия:
            {{ data_model.sellerPassNumberFirst }} номер:
            {{ data_model.sellerPassNumberSec }}, выдан:
            {{ data_model.sellerPassIssuedBy.toUpperCase() }}
            {{ data_model.sellerPassIssuedOn }}, код
            подразделения: {{ data_model.sellerUnitCode }},
            зарегистрированный по адресу
            {{ data_model.sellerRegAddress }}
            <span v-if="JSON.stringify(data_model.sellerRepresent).match('Да, от имени Продавца действует представитель')">
            , в лице Представителя на основании доверенности №{{ data_model.sellerRepresentDocNum }}
            от {{ data_model.sellerRepresentDocDate }}, выданной
            {{ data_model.sellerRepresentDocBy }} на имя
            {{ data_model.sellerRepresentFullName }}. Данные доверенности:
            Паспортные данные: серия:
            {{ data_model.sellerRepresentPassNumFirst }}, номер:
            {{ data_model.sellerRepresentDocPassNumSec }}, выдан:
            {{ data_model.sellerRepresentPassIssuedBy }},
            {{ data_model.sellerRepresentPassDate }}, код подразделения:
            {{ data_model.sellerRepresentUnitCode }}, адрес регистрации:
            {{ data_model.sellerRepresentRegAddress }}</span>, именуемый в дальнейшем
            <b>Продавец</b>, с одной стороны, и
          </p>
        </div>
        <div v-else-if="select_second_step == 'ЮЛ'">
          <p>
            <b
              >{{ data_model.sellerOrgLegalForm }} "{{
                data_model.sellerOrgName.toUpperCase()
              }}"</b
            >
            в лице {{ data_model.sellerOrgPossition }}
            {{ data_model.sellerCeoFullName }}, действующего на
            основании {{ data_model.sellerOrgDoc.firstLetterCaps() }}
            <span v-if="JSON.stringify(data_model.sellerOrgDoc).toLowerCase().match('доверенности')">
            №{{ data_model.sellerOrgDocNum }} от
            {{ data_model.sellerOrgDocDate }}.
            <br>
            Паспортные данные представителя: серия:
            {{ data_model.sellerOrgDocPassNumFirst }}, номер:
            {{ data_model.sellerOrgDocPassNumSec }}, выдан:
            {{ data_model.sellerOrgPassIssuedBy }},
            {{ data_model.sellerOrgDocPassDate }}, код подразделения:
            {{ data_model.sellerOrgUnitCode }}, адрес регистрации:
            {{ data_model.sellerOrgRegAddress }},</span> с одной стороны, и
          </p>
        </div>
      </div>
      <div v-if="select_third_step == 'ФЛ'">
        <p>
          {{ data_model.custFullName }},
          {{ data_model.custBirthYear }} года рождения,
          место рождения: {{ data_model.custBirthPlace }},
          гражданство: {{ data_model.custNationality }}, паспорт
          серия: {{ data_model.custPassNumberFirst }} номер:
          {{ data_model.custPassNumberSec }}, выдан:
          {{ data_model.custPassIssuedBy.toUpperCase() }}
          {{ data_model.custPassIssuedOn }}, код
          подразделения: {{ data_model.custUnitCode }},
          зарегистрированный по адресу
          {{ data_model.custRegAddress }}
          <span v-if="JSON.stringify(data_model.custRepresent).match('Да, от имени Покупателя действует представитель')">
            , в лице Представителя на основании доверенности №{{ data_model.custRepresentDocNum }}
            от {{ data_model.custRepresentDocDate }}, выданной
            {{ data_model.custRepresentDocBy }} на имя
            {{ data_model.custRepresentFullName }}. Данные доверенности:
            Паспортные данные: серия:
            {{ data_model.custRepresentPassNumFirst }}, номер:
            {{ data_model.custRepresentDocPassNumSec }}, выдан:
            {{ data_model.custRepresentPassIssuedBy }},
            {{ data_model.custRepresentPassDate }}, код подразделения:
            {{ data_model.custRepresentUnitCode }}, адрес регистрации:
            {{ data_model.custRepresentRegAddress }}</span>,
            именуемый в дальнейшем
          <b>Покупатель</b>, с другой стороны, совместно именуемые
          <b>Стороны, заключили настоящий договор о нижеследующем:</b>
        </p>
      </div>
      <div v-else-if="select_third_step == 'ЮЛ'">
        <p>
          <b
            >{{ data_model.custOrgLegalForm }} "{{
              data_model.custOrgName.toUpperCase()
            }}"</b
          >
          в лице {{ data_model.custOrgPossition }}
          {{ data_model.custCeoFullName }}, действующего на основании
          {{ data_model.custOrgDoc.firstLetterCaps() }}
          <span v-if="JSON.stringify(data_model.custOrgDoc).toLowerCase().match('доверенности')">
            №{{ data_model.custOrgDocNum }} от
            {{ data_model.custOrgDocDate }}.
            <br>
            Паспортные данные представителя: серия:
            {{ data_model.custOrgDocPassNumFirst }}, номер:
            {{ data_model.custOrgDocPassNumSec }}, выдан:
            {{ data_model.custOrgPassIssuedBy }},
            {{ data_model.custOrgDocPassDate }}, код подразделения:
            {{ data_model.custOrgUnitCode }}, адрес регистрации:
            {{ data_model.custOrgRegAddress }}</span>, именуемый в дальнейшем
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
      <div v-for="(one, index) in model.propertyName" :key="index">
        <p v-if="data_model.propertyName[index] == 'Квартира'">
          {{ data_model.propertyName[index] | str_corr }}, общей площадью
          {{ data_model.propertyFloorArea[index] | str_corr }} кв.м, количество комнат:
          {{ data_model.propertyNumRoom[index] | str_corr }}, этаж:
          {{ data_model.propertyLevel[index] | str_corr }}, расположенная по адресу:
          {{ data_model.propertyAddress[index] | str_corr }}, кадастровый номер:
          {{ data_model.propertyUniqueIdentifier[index] | str_corr }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ data_model.propertyDoc[index] | str_corr }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ data_model.propertyRegDocDate[index] | date_corr | str_corr }} №{{
            data_model.propertyRegDocNumber[index] | str_corr
          }}.
        </p>
        <p v-else-if="data_model.propertyName[index] == 'Земельный участок'">
          {{ data_model.propertyName[index] | str_corr }}, общей площадью
          {{ data_model.propertyFloorArea[index] | str_corr }} кв.м, категория земель:
          {{ data_model.propertyLandCat[index] | str_corr }}, разрешенное
          использование: {{ data_model.propertyLandUsed[index] | str_corr }},
          расположенный по адресу: {{ data_model.propertyAddress[index] | str_corr }},
          кадастровый номер:
          {{ data_model.propertyUniqueIdentifier[index] | str_corr }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ data_model.propertyDoc[index] | str_corr }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ data_model.propertyRegDocDate[index] | date_corr | str_corr }} №{{
            data_model.propertyRegDocNumber[index] | str_corr
          }}.
        </p>
        <p v-else-if="data_model.propertyName[index] == 'Жилой дом'">
          {{ data_model.propertyName[index] | str_corr }}, общей площадью
          {{ data_model.propertyFloorArea[index] | str_corr }} кв.м, количество комнат:
          {{ data_model.propertyNumRoom[index] | str_corr }}, этажей:
          {{ data_model.propertyLevel[index] | str_corr }}, расположенный по адресу:
          {{ data_model.propertyAddress[index] | str_corr }}, кадастровый номер:
          {{ data_model.propertyUniqueIdentifier[index] | str_corr }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ data_model.propertyDoc[index] | str_corr }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ data_model.propertyRegDocDate[index] | date_corr | str_corr }} №{{
            data_model.propertyRegDocNumber[index] | str_corr
          }}.
        </p>
        <p v-else-if="data_model.propertyName[index] == 'Нежилое здание'">
          {{ data_model.propertyName[index] | str_corr }}, общей площадью
          {{ data_model.propertyFloorArea[index] | str_corr }} кв.м,
          расположенное по адресу: {{ data_model.propertyAddress[index] | str_corr }},
          кадастровый номер:
          {{ data_model.propertyUniqueIdentifier[index] | str_corr }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ data_model.propertyDoc[index] | str_corr }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ data_model.propertyRegDocDate[index] | date_corr | str_corr }} №{{
            data_model.propertyRegDocNumber[index] | str_corr
          }}.
        </p>
        <p v-if="data_model.propertyName[index] == 'Нежилое помещение'">
          {{ data_model.propertyName[index] | str_corr }}, общей площадью
          {{ data_model.propertyFloorArea[index] | str_corr }} кв.м, этаж:
          {{ data_model.propertyLevel[index] | str_corr }}, расположенная по адресу:
          {{ data_model.propertyAddress[index] | str_corr }}, кадастровый номер:
          {{ data_model.propertyUniqueIdentifier[index] | str_corr }}. Данный объект
          принадлежит <b>Продавцу</b> на основании
          {{ data_model.propertyDoc[index] | str_corr }}, о чем в Едином
          государственном реестре недвижимости сделана запись регистрации от
          {{ data_model.propertyRegDocDate[index] | date_corr | str_corr }} №{{
            data_model.propertyRegDocNumber[index] | str_corr
          }}.
        </p>
      </div>
      <div>
        <p>
          <b>2.</b> Стоимость недвижимого имущества составляет
          <b
            >{{ data_model.cost | numeral("₽0,0.00") }} ({{
              data_model.cost | rubles
            }})</b
          >. Цена является окончательной и изменению не подлежит. Расчет между
          сторонами осуществляется в следующем порядке:
        </p>
      </div>
      <div v-if="JSON.stringify(data_model.payMethod).match('Материнский капитал')">
        <p>
          Оплата суммы в размере
          <b
            >{{ data_model.paySumMatCap | numeral("₽0,0.00") }} ({{
              data_model.paySumMatCap | rubles
            }})</b
          >
          осуществляется <b>Покупателем</b> за счет средств
          <b>государственного сертификата на материнский (семейный) капитал</b>,
          выданного на основании решения
          <b>{{ data_model.matcap.toUpperCase() }}</b> от
          {{ data_model.matcapDesDate }} №
          {{ data_model.matcapDesNum }}, серии
          {{ data_model.matcapSer }} №
          {{ data_model.matcapNum }}, выданного
          {{ data_model.matcapDate }} на имя
          <b>{{ data_model.matcapOwner }}</b
          >, в соответствии с Федеральным законом
          <b
            >«О дополнительных мерах государственной поддержки семей, имеющих
            детей»</b
          >, после государственной регистрации перехода права собственности на
          имя <b>Покупателя</b>, в установленный законом срок.
        </p>
      </div>
      <div v-if="JSON.stringify(data_model.payMethod).match('Рассрочка')">
        <p>
          Денежные средства в размере
          <b
            >{{ data_model.paySumRS | numeral("₽0,0.00") }} ({{
              data_model.paySumRS | rubles
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
                {{ item.toLocaleDateString() }}
              </p>
            </td>
            <td>
              <b>{{ model.rsPayment[one] | numeral("₽0,0.00") }}</b>
            </td>
          </tr>
        </table>
        <div v-if="JSON.stringify(data_model.payMethod).match('Рассрочка')">
          <span
            >Оплата по договору осуществляется в срок до
            {{ data_model.zlgPayTermDate }}</span
          >
        </div>
        <div v-if="JSON.stringify(data_model.payMethod).match('Рассрочка')">
          <p v-if="data_model.zlgPay == 'Имеется'">
            Стороны договорились о том, что до полного расчета по основному
            договору купли-продажи право залога на отчуждаемую квартиру в силу
            закона (в соответствии с ч. 5 ст. 488 Гражданского кодекса РФ)
            устанавливается в пользу «Продавца».
          </p>
          <p v-else-if="data_model.zlgPay == 'Не имеется'">
            Стороны договорились о том, что до полного расчета по основному
            договору купли-продажи право залога на отчуждаемую квартиру в силу
            закона (в соответствии с ч. 5 ст. 488 Гражданского кодекса РФ) в
            пользу «Продавца» не возникает.
          </p>
        </div>
      </div>

      <div v-if="JSON.stringify(data_model.payMethod).match('Ипотека физ. лица')">
        <p>
          Денежные средства в размере
          <b
            >{{ model.paySumFL | numeral("₽0,0.00") }} ({{
              data_model.paySumFL | rubles
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
                {{ item.toLocaleDateString() }}
              </p>
            </td>
            <td>
              <b>{{ model.rsPaymentFL[one] | numeral("₽0,0.00") }}</b>
            </td>
          </tr>
        </table>
        <div v-if="JSON.stringify(data_model.payMethod).match('Ипотека физ. лица')">
          <span
            >Оплата по договору осуществляется в срок до
            {{ data_model.zlgPayTermDate }}</span
          >
        </div>
        <div v-if="JSON.stringify(data_model.payMethod).match('Ипотека физ. лица')">
          <p>
            Стороны договорились о том, что до полного расчета по основному
            договору купли-продажи право залога на отчуждаемую квартиру в силу
            закона (в соответствии с ч. 5 ст. 488 Гражданского кодекса РФ)
            устанавливается в пользу «Продавца».
          </p>
        </div>
      </div>

      <div v-if="JSON.stringify(data_model.payMethod).match('Наличный расчет')">
        <p>
          Оплата стоимости имущества в размере
          <b
            >{{ data_model.nal | numeral("₽0,0.00") }} ({{
              data_model.nal | rubles
            }})</b
          >
          осуществляется <b> Покупателем</b> за счет собственных наличных
          денежных средств.
        </p>
      </div>

      <div v-if="JSON.stringify(data_model.payMethod).match('Безналичный расчет')">
        <p>
          Оплата стоимости имущества в размере
          <b
            >{{ data_model.bznal | numeral("₽0,0.00") }} ({{
              data_model.bznal | rubles
            }})</b
          >
          осуществляется <b> Покупателем</b> за счет собственных наличных
          денежных средств путем перечисления указанной суммы на счет
          <b>Продавца</b> № {{ data_model.bznalBankNum }}, открытый в
          {{ data_model.bznalBankName }}.
        </p>
      </div>

      <div v-if="JSON.stringify(data_model.payMethod).match('Ипотека банка')">
        <p>
          Оплата суммы в размере
          <b
            >{{ data_model.paySumIB | numeral("₽0,0.00") }} ({{
              data_model.paySumIB | rubles
            }})</b
          >
          осуществляется <b>Покупателем</b> за счет кредитных средств
          предоставленных
          <b>Покупателю {{ data_model.crBankName.toUpperCase() }}</b>
          (далее - Банк), в соответствии с кредитным договором №
          {{ data_model.crBankNumber }} от
          <b>{{ data_model.crBankDocDate }}</b
          >, заключенным в городе
          {{ data_model.crBankDocTown }} между Банком и
          <b>Покупателем</b> (далее – Кредитный договор) сроком на
          <b>{{ data_model.crBankDocQMonth }}</b>
          {{ data_model.crBankDocQMonth | months }} под процентную ставку Банка.
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
            >{{ data_model.crBankName.toUpperCase() }} (РЕКВИЗИТЫ
            БАНКА: ОГРН: {{ data_model.crBankOgrn }}, ИНН:
            {{ data_model.crBankInn }}, КПП:
            {{ data_model.crBankKpp }}, Р/С:
            {{ data_model.crBankRs }}, К/С:
            {{ data_model.crBankKs }}, БИК:
            {{ data_model.crBankBik }}, Местонахождение банка:
            {{ data_model.crBankAddress }}, Почтовый адрес банка:
            {{ data_model.crBankPostAddress }})</b
          >
          Залогодателем – Покупатель.
          <br />
          <br />
          Права Залогодержателя удостоверяются закладной.
        </p>
      </div>
      <div v-if="JSON.stringify(data_model.payMethod).match('Аккредитив')">
        <p>
          Оплата суммы в размере
          <b
            >{{ data_model.paySumA | numeral("₽0,0.00") }} ({{
              data_model.paySumA | rubles
            }})</b
          >
          осуществляется <b>Покупателем</b> путем открытия документарного
          безотзывного покрытого аккредитива на сумму
          <b
            >{{ data_model.paySumA | numeral("₽0,0.00") }} ({{
              data_model.paySumA | rubles
            }})</b
          >
          в пользу <b>Продавца </b> в день подписания настоящего договора,
          сроком действия {{ data_model.acrDays }}
          {{ data_model.acrDays | days }} со дня подписания
          настоящего договора (далее – «Аккредитив»). Покрытие аккредитива
          осуществляется <b>Покупателем</b> за счет собственных средств.
        </p>
        <br />
        <p>
          Банком – эмитентом и исполняющим банком по аккредитиву является
          {{ data_model.acrBankName.toUpperCase() }} (далее – «Банк»)
          в г. {{ data_model.acrBankTown.firstLetterCaps() }}
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
          <b>Продавца</b> № {{ data_model.acrBankSellerNumber }},
          открытый в
          {{ data_model.acrBankSellerName.toUpperCase() }} (далее –
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
        <p v-if="JSON.stringify(data_model.propertyName).match('Квартира')">
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
            {{ data_model.sellerFullName }}
          </p>
        </div>
        <div class="rf" v-if="select_third_step == 'ФЛ'">
          <p>
            <b>Покупатель:</b>
          </p>
          <p>
            {{ data_model.custFullName }}
          </p>
        </div>
        <div class="lf" v-if="select_second_step == 'ЮЛ'">
          <p>
            <b>Продавец:</b>
          </p>
          <p>
            {{ data_model.sellerOrgLegalForm }} "{{
              data_model.sellerOrgName
            }}"
          </p>
          <p>
            Юридический адрес: {{ data_model.sellerOrgRegAddressUR }}
          </p>
          <p>ОГРН: {{ data_model.sellerOrgOGRN }}</p>
          <p>ИНН: {{ data_model.sellerOrgINN }}</p>
          <p>КПП: {{ data_model.sellerOrgKPP }}</p>
          <p>Р/С: {{ data_model.sellerOrgRS }}</p>
          <p>КС: {{ data_model.sellerOrgKS }}</p>
          <p>Банк: {{ data_model.sellerOrgBank }}</p>
          <p>БИК: {{ data_model.sellerOrgBankBik }}</p>
          <p>Номер телефона: {{ data_model.sellerOrgTel }}</p>
          <p>
            Почтовый адрес: {{ data_model.sellerOrgPostAddress }}
          </p>
          <p>В лице: {{ data_model.sellerCeoFullName }}</p>
        </div>
        <div class="rf" v-if="select_third_step == 'ЮЛ'">
          <p>
            <b>Покупатель:</b>
          </p>
          <p>
            {{ data_model.custOrgLegalForm }} "{{
              data_model.custOrgName
            }}"
          </p>
          <p>
            Юридический адрес: {{ data_model.custOrgRegAddressUR }}
          </p>
          <p>ОГРН: {{ data_model.custOrgOGRN }}</p>
          <p>ИНН: {{ data_model.custOrgINN }}</p>
          <p>КПП: {{ data_model.custOrgKPP }}</p>
          <p>Р/С: {{ data_model.custOrgRS }}</p>
          <p>КС: {{ data_model.custOrgKS }}</p>
          <p>Банк: {{ data_model.custOrgBank }}</p>
          <p>БИК: {{ data_model.custOrgBankBik }}</p>
          <p>Номер телефона: {{ data_model.custOrgTel }}</p>
          <p>Почтовый адрес: {{ data_model.custOrgPostAddress }}</p>
          <p>В лице: {{ data_model.custFullName }}</p>
        </div>
      </div>

      <div
        class="receipt"
        v-if="JSON.stringify(data_model.payMethod).match('Наличный расчет')"
      >
        <div id="header">
          <p>
            <strong
              >Расписка о получении денежных средств в счет оплаты по договору
              купли-продажи № {{ data_model.number }} от
              {{ data_model.date }} г.
            </strong>
          </p>
        </div>
        <div id="date">
          <p id="left">
            <strong
              >Город: {{ data_model.city.firstLetterCaps() }}</strong
            >
          </p>
          <p id="right">
            <strong>Дата: {{ data_model.date }}</strong>
          </p>
        </div>
        <p>
          Гр. {{ data_model.sellerFullName }}, именуемый в дальнейшем
          <b>«Продавец»</b> и
        </p>
        <p>
          Гр. {{ data_model.custFullName }}, именуемый в дальнейшем
          <b>«Покупатель»</b>, с другой стороны, совместно именуемые
          <b>«Стороны»</b>,
        </p>
        <br />
        <p>составили настоящую расписку о нижеследующем:</p>
        <br />
        <p>
          <b>1. «Покупатель»</b> передал, а <b>«Продавец»</b> принял денежные
          средства в размере
          <b
            >{{ data_model.nal | numeral("₽0,0.00") }} ({{
              data_model.nal | rubles
            }})</b
          >
          в счет оплаты следующего недвижимого имущества: <br><br> 
          <span v-for="(item, index) in data_model.propertyName" :key="index">{{ '1.' + (index + 1) + '. ' + item + ', ' }}
          общей площадью {{ data_model.propertyFloorArea[index] }} кв.м;<br>
          </span>
          <br>
          по Договору купли-продажи № {{ data_model.number }} от
          {{ data_model.date }} г., заключенному между
          <b>«Продавцом»</b> и <b>«Покупателем»</b>.
        </p>
        <br />
        <p>
          <b>2. «Стороны»</b> подтверждают, что оплата по Договору произведена в
          полном объеме. Претензии по оплате у Сторон отсутствуют.
        </p>
        <br />
        <p v-if="JSON.stringify(data_model.avance).match('Имеется')">
          <b>3. «Продавец»</b> подтверждает, что авансовый платеж в размере
          <b
            >{{ data_model.avancesum | numeral("₽0,0.00") }} ({{
              data_model.avancesum | rubles
            }})</b
          >
          был передан <b>«Покупателем» «Продавцу»</b> до подписания Договора
          купли-продажи недвижимого имущества №
          {{ data_model.number }} от
          {{ data_model.date }} г.
        </p>
        <br />
        <div class="lf" v-if="select_second_step == 'ФЛ'">
          <p>
            <b>Продавец:</b>
          </p>
          <p>_______________________</p>
          <p>Гр. {{ data_model.sellerFullName }}</p>
        </div>
        <div class="rf" v-if="select_third_step == 'ФЛ'">
          <p>
            <b>Покупатель:</b>
          </p>
          <p>_______________________</p>
          <p>Гр. {{ data_model.custFullName }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="module">
/* eslint-disable */
import Vue from "vue";

const plural = require('plural-ru');

String.prototype.firstLetterCaps = function () {
  return this.charAt(0).toUpperCase() + this.slice(1);
};

Vue.filter("date_corr", function (value) {
  if (value instanceof Date) return value.toLocaleDateString()
})

Vue.filter("str_corr", function (value) {
  if (!value) return "_________________"
  return value
})

let rubles = require("rubles").rubles;
Vue.filter("rubles", function (value) {
  if (value == '_________________') return "_________________";
  return rubles(value);
});

Vue.filter("months", function (value) {
  return plural(value, 'месяц', 'месяца', 'месяцев')
});

Vue.filter("days", function (value) {
  return plural(value, 'день', 'дня', 'дней')
});

export default {
  name: "dogovor_kupli_prodazhi",
  props: {
    model: Object,
    schema: Object,
    select_second_step: String,
    select_third_step: String,
    plain: Function,
    add: Boolean,
    quantityOfProperty: Number,
  },
  data() {
    return {
      data_model: null
    }
  },
  created() {
    this.data_model = JSON.parse(JSON.stringify(this.model))
    for (let i in this.data_model) {
      this.data_model[i] = '_________________';
      this.data_model.propertyRegDocDate = [];
    }
  },
  watch: {
    model: {
      deep: true,
      handler(newValue) {
        for (let i in newValue) {
          if (newValue[i]) {
            this.data_model[i] = newValue[i]
          }
          if (newValue[i] instanceof Date) {
            this.data_model[i] = newValue[i].toLocaleDateString();
          }
        }
      },
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
