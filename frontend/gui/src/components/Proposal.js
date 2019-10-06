import React from 'react';
import { Rail, Segment, Header, Progress, Statistic, Icon, Label, Container} from 'semantic-ui-react'
import Countdown from "./Countdown";


const Proposals = (props) => {

    function checkColor(a, b) {
        if (a < b) {
            return "yellow"
        } else {
            return "red"
        }
    }


    return (

        <div>

            {props.data.map(item => (
                <div>
                    <br/><br/>
                    <Segment.Group stacked key={item.id} piled raised>

                        <Segment padded>

                            <Label as='a' color='red' tag attached={"top right"}>
                                <Icon name={"futbol"}/>
                                Sport
                            </Label>

                            {
                                <a href={`/markets/${item.id}`}>
                                    <Header as='h2' textAlign={"center"}>
                                        {/*<Image floated={"left"} circular src='https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png' />*/}
                                        {item.name}
                                    </Header>
                                </a>
                            }

                        </Segment>

                        <Segment padded size={"huge"}>
                            <Container text textAlign={"center"}>
                                <p>
                                    {item.description}
                                </p>
                            </Container>
                        </Segment>

                        <Segment>
                            <Label attached='bottom' ribbon>
                                <Statistic.Group size={"mini"}>

                                    <Statistic>
                                        <Statistic.Value>
                                            <Label attached={"bottom"}>{item.end_date}</Label>
                                        </Statistic.Value>
                                    </Statistic>

                                    <Statistic>
                                        <Statistic.Value>
                                            <Label attached={"bottom left"}>Supply: {item.supply} <Icon name={"bolt"}/></Label>
                                        </Statistic.Value>
                                    </Statistic>

                                    <Statistic>
                                        <Statistic.Value>
                                            <Countdown date={item.end_date}/>
                                        </Statistic.Value>
                                    </Statistic>

                                </Statistic.Group>
                            </Label>

                        </Segment>

                        <Progress percent={new Date(Date.now()).getDate() * 100 / new Date(item.end_date).getDate()}
                                  attached={"bottom"}
                                  color={checkColor(new Date(Date.now()).getDate(), new Date(item.end_date).getDate())}/>

                        <Rail dividing position='right'>
                            <Segment>Right Rail Content</Segment>
                        </Rail>

                    </Segment.Group>
                </div>

            ))}

        </div>

    )
};

export default Proposals;